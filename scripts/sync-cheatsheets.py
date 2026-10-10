#!/usr/bin/env python3
"""Build the committed Cloudflare Pages site from local HTML and ZIP cheatsheets."""

import argparse
import html
import shutil
import stat
import tempfile
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urlsplit
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ""
        self.links = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.links.append(values[attribute])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def parse_page(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser


def extract_pack(archive, destination):
    with ZipFile(archive) as zip_file:
        seen = set()
        for entry in zip_file.infolist():
            name = entry.filename
            path = PurePosixPath(name)
            mode = (entry.external_attr >> 16) & 0o170000
            if (not name or "\\" in name or path.is_absolute()
                    or ".." in path.parts or path.parts[0] != archive.stem
                    or mode == stat.S_IFLNK):
                raise ValueError(f"Unsafe ZIP entry in {archive.name}: {name}")
            if path in seen:
                raise ValueError(f"Duplicate ZIP entry in {archive.name}: {name}")
            seen.add(path)
            target = destination.joinpath(*path.parts)
            if entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if target.exists():
                raise ValueError(f"Output path collision: {target.relative_to(destination)}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with zip_file.open(entry) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output)
    index = destination / archive.stem / "index.html"
    if not index.is_file():
        raise ValueError(f"ZIP pack has no entry page: {archive.name}")
    return index


def copy_directory(source, destination):
    target_root = destination / source.name
    if target_root.exists():
        raise ValueError(f"Output path collision: {source.name}")
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Source contains a symlink: {path}")
        target = target_root / path.relative_to(source)
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        else:
            raise ValueError(f"Unsupported source entry: {path}")
    return target_root / "index.html"


def render_index(standalone, packs):
    def section(title, entries):
        items = "\n".join(
            f'<li><a href="{html.escape(url, quote=True)}">'
            f'{html.escape(label)}</a></li>' for label, url in entries
        )
        return f"<section><h2>{title}</h2><ul>{items}</ul></section>"

    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tech cheatsheets</title>
<style>
  :root {{ color-scheme: light dark; font-family: system-ui, sans-serif; }}
  body {{ max-width: 54rem; margin: 3rem auto; padding: 0 1.25rem; line-height: 1.5; }}
  h1 {{ margin-bottom: .25rem; }}
  section {{ margin-top: 2rem; }}
  ul {{ list-style: none; padding: 0; display: grid; gap: .75rem; }}
  li {{ border: 1px solid #8888; border-radius: .5rem; }}
  a {{ display: block; padding: .8rem 1rem; color: inherit; }}
  a:hover, a:focus-visible {{ background: #8882; }}
</style>
<main>
  <h1>Tech cheatsheets</h1>
  <p>Browse the generated guides and illustrated packs.</p>
  {section("Standalone guides", standalone)}
  {section("Illustrated packs", packs)}
</main>
</html>
"""


def broken_links(site):
    root = site.resolve()
    for page in sorted(site.rglob("*.html")):
        for link in parse_page(page).links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = unquote(parsed.path).lstrip("/")
            target = (site / relative if parsed.path.startswith("/")
                      else page.parent / relative).resolve()
            if not target.is_relative_to(root):
                yield page.relative_to(site), link
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                yield page.relative_to(site), link


def build(source, destination):
    inputs = sorted(p for p in source.iterdir() if not p.name.startswith("."))
    if not inputs:
        raise ValueError(f"No cheatsheets found in {source}")
    standalone, packs = [], []
    for path in inputs:
        if path.is_symlink():
            raise ValueError(f"Unsupported source entry: {path.name}")
        if path.is_dir():
            index = copy_directory(path, destination)
            if index.is_file():
                title = parse_page(index).title.strip() or path.name
                packs.append((title, "/" + quote(path.name) + "/"))
        elif path.suffix.lower() == ".html":
            target = destination / path.name
            if target.exists() or path.name in ("index.html", "404.html"):
                raise ValueError(f"Output path collision: {path.name}")
            shutil.copyfile(path, target)
            title = parse_page(target).title.strip() or path.stem
            standalone.append((title, "/" + quote(path.name)))
        elif path.suffix.lower() == ".zip":
            index = extract_pack(path, destination)
            title = parse_page(index).title.strip() or path.stem
            packs.append((title, "/" + quote(path.stem) + "/"))
        else:
            raise ValueError(f"Unsupported source file: {path.name}")
    (destination / "index.html").write_text(render_index(standalone, packs), encoding="utf-8")
    (destination / "404.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<title>Page not found</title><h1>Page not found</h1>'
        '<p><a href="/">Browse cheatsheets</a></p></html>\n', encoding="utf-8")
    return len(standalone), len(packs), list(broken_links(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Folder of HTML and ZIP cheatsheets")
    args = parser.parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        parser.error(f"Source directory does not exist: {source}")
    with tempfile.TemporaryDirectory(prefix=".cheatsheets-sync-", dir=ROOT) as temporary:
        staging = Path(temporary) / "site"
        staging.mkdir()
        standalone_count, pack_count, missing = build(source, staging)
        backup = Path(temporary) / "previous-site"
        if SITE.exists():
            SITE.rename(backup)
        try:
            staging.rename(SITE)
        except OSError:
            if backup.exists():
                backup.rename(SITE)
            raise
    count = sum(path.is_file() for path in SITE.rglob("*"))
    print(f"Built {SITE}: {standalone_count} standalone pages, {pack_count} packs, {count} files")
    for page, link in missing:
        print(f"WARNING missing local link: {page} -> {link}")
    print(f"Missing local links: {len(missing)}")


if __name__ == "__main__":
    main()
