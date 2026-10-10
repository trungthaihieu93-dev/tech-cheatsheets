# Cloudflare Pages deployment

This public site serves the generated cheatsheets from `site/`. That directory is
committed to Git so Cloudflare Pages can deploy it without access to the local
source folder. Original ZIP downloads are not published; each pack is extracted
into a browsable directory.

Live site: [tech-cheatsheets.pages.dev](https://tech-cheatsheets.pages.dev/).
The production branch is `master` in
[trungthaihieu93-dev/tech-cheatsheets](https://github.com/trungthaihieu93-dev/tech-cheatsheets).

## Refresh the site

Run from the repository root, changing the source path if needed:

```sh
python3 scripts/sync-cheatsheets.py --source /home/tonythai93/Documents/cheatsheets
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
git status --short
```

The command copies top-level HTML files and supporting directories, extracts
every top-level ZIP pack, generates the catalog and 404 page, and removes files
from `site/` that are no longer in the source. A directory with an `index.html`
is listed as a pack. It fails on unsupported source files or unsafe ZIP entries.
Review `site/` before committing: the GitHub repository and Pages site are both
public, including the personal interview page.

Commit and push the refreshed files to publish them:

```sh
git add .gitignore scripts/sync-cheatsheets.py tests/test_sync_cheatsheets.py site docs/cloudflare-deployment.md
git commit -m "feat: publish cheatsheet library"
git push -u origin master
```

For later refreshes, stage the updated `site/` files and any related source or
documentation changes, then commit and push. A local file change alone does not
trigger a Pages deployment.

## Connect Cloudflare Pages

1. In **Workers & Pages**, create a Pages project using **Import an existing Git repository**.
2. Connect `trungthaihieu93-dev/tech-cheatsheets` and select `master` as the production branch.
3. Choose no framework preset, set the build command to `exit 0`, and set the output directory to `site`.
4. Use `tech-cheatsheets` as the project name if available. The site will be served at the assigned `*.pages.dev` address. Subsequent pushes to `master` redeploy it.

Cloudflare Pages requires a root `index.html`; the sync command generates it.
It also generates a root `404.html` so missing paths return a 404 instead of the
default single-page fallback.

The current Go standalone page links to eight topic pages absent from the
source folder. Sync reports them as warnings and publishes the page unchanged.
Add those topic pages to the source when they become available, then sync again.

References: [static HTML deployment](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/),
[Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/),
[Pages route and 404 behavior](https://developers.cloudflare.com/pages/configuration/serving-pages/).
