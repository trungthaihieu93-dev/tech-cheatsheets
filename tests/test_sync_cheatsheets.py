"""Tests for the local cheatsheet site builder."""

import contextlib
import importlib.util
import io
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile, ZipInfo


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync-cheatsheets.py"
SPEC = importlib.util.spec_from_file_location("sync_cheatsheets", SCRIPT)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class SyncCheatsheetsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.site = self.root / "site"

    def write_source(self, name, content):
        path = self.source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_zip(self, name, entries):
        archive = self.source / name
        with ZipFile(archive, "w") as zipped:
            for path, content in entries.items():
                zipped.writestr(path, content)
        return archive

    def run_command(self):
        output = io.StringIO()
        with (patch.object(sync, "ROOT", self.root),
              patch.object(sync, "SITE", self.site),
              patch.object(sys, "argv", [str(SCRIPT), "--source", str(self.source)]),
              contextlib.redirect_stdout(output)):
            sync.main()
        return output.getvalue()

    def site_files(self):
        return {str(path.relative_to(self.site)): path.read_bytes()
                for path in self.site.rglob("*") if path.is_file()}

    def test_builds_catalog_and_copies_html_zip_and_support_assets(self):
        self.write_source("Quick & Easy.html", """<title>Tips &amp; tricks</title>
<link href="support/theme.css"><img src="support/chart.svg">
<a href="/visual-pack/">Illustrated pack</a>""")
        self.write_source("support/theme.css", "body { color: teal; }")
        self.write_source("support/chart.svg", "<svg></svg>")
        self.write_zip("visual-pack.zip", {
            "visual-pack/index.html": '<title>Visual < Guide</title><img src="img/chart.png">',
            "visual-pack/img/chart.png": b"\x89PNG\r\n",
        })
        self.site.mkdir()

        standalone, packs, missing = sync.build(self.source, self.site)

        self.assertEqual((standalone, packs, missing), (1, 1, []))
        catalog = (self.site / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="/Quick%20%26%20Easy.html"', catalog)
        self.assertIn("Tips &amp; tricks", catalog)
        self.assertIn('href="/visual-pack/"', catalog)
        self.assertIn("Visual &lt; Guide", catalog)
        self.assertEqual((self.site / "support/theme.css").read_text(),
                         "body { color: teal; }")
        self.assertEqual((self.site / "visual-pack/img/chart.png").read_bytes(),
                         b"\x89PNG\r\n")
        self.assertTrue((self.site / "404.html").is_file())

    def test_directory_with_entry_page_is_a_pack_and_support_directory_is_not(self):
        self.write_source("folder-pack/index.html", '<title>Folder pack</title><a href="pages/next.html">Next</a>')
        self.write_source("folder-pack/pages/next.html", "<title>Next</title>")
        self.write_source("shared/icons/icon.svg", "<svg></svg>")
        self.site.mkdir()

        self.assertEqual(sync.build(self.source, self.site), (0, 1, []))
        catalog = (self.site / "index.html").read_text()
        self.assertIn('href="/folder-pack/"', catalog)
        self.assertNotIn('href="/shared/"', catalog)
        self.assertTrue((self.site / "shared/icons/icon.svg").is_file())

    def test_rejects_traversal_absolute_backslash_and_symlink_zip_entries(self):
        cases = {
            "parent": "pack/../../escape.txt",
            "absolute": "/pack/escape.txt",
            "backslash": "pack\\escape.txt",
        }
        for label, unsafe_name in cases.items():
            with self.subTest(label=label):
                archive = self.write_zip("pack.zip", {
                    "pack/index.html": "<title>Pack</title>",
                    unsafe_name: "bad",
                })
                destination = self.root / label
                destination.mkdir()
                with self.assertRaisesRegex(ValueError, "Unsafe ZIP entry"):
                    sync.extract_pack(archive, destination)
                self.assertFalse((self.root / "escape.txt").exists())

        symlink = ZipInfo("pack/outside")
        symlink.create_system = 3
        symlink.external_attr = (stat.S_IFLNK | 0o777) << 16
        archive = self.write_zip("pack.zip", {
            "pack/index.html": "<title>Pack</title>",
            symlink: "../../outside",
        })
        destination = self.root / "symlink"
        destination.mkdir()
        with self.assertRaisesRegex(ValueError, "Unsafe ZIP entry"):
            sync.extract_pack(archive, destination)
        self.assertFalse((destination / "pack/outside").exists())

    def test_replaces_stale_site_and_repeated_runs_are_identical(self):
        self.write_source("old.html", "<title>Old</title>")
        self.site.mkdir()
        (self.site / "stale.html").write_text("old site")

        first_output = self.run_command()
        first_files = self.site_files()
        self.assertIn("1 standalone pages, 0 packs", first_output)
        self.assertNotIn("stale.html", first_files)
        self.assertIn("old.html", first_files)

        self.run_command()
        self.assertEqual(self.site_files(), first_files)

        (self.source / "old.html").unlink()
        self.write_source("new.html", "<title>New</title>")
        self.run_command()
        self.assertNotIn("old.html", self.site_files())
        self.assertIn("new.html", self.site_files())

    def test_invalid_pack_keeps_previous_site(self):
        self.site.mkdir()
        (self.site / "existing.html").write_text("keep me")
        self.write_zip("bad.zip", {
            "bad/index.html": "<title>Bad</title>",
            "bad/../../escape.txt": "bad",
        })

        with self.assertRaisesRegex(ValueError, "Unsafe ZIP entry"):
            self.run_command()
        self.assertEqual(self.site_files(), {"existing.html": b"keep me"})
        self.assertFalse((self.root / "escape.txt").exists())

    def test_missing_relative_link_warns_without_failing_sync(self):
        self.write_source("page.html", '<title>Page</title><link href="missing.css">')

        output = self.run_command()

        self.assertTrue((self.site / "page.html").is_file())
        self.assertIn("WARNING missing local link: page.html -> missing.css", output)
        self.assertIn("Missing local links: 1", output)


if __name__ == "__main__":
    unittest.main()
