# Cloudflare cheatsheet library

Status: In progress

## Outcome

Publish all five standalone HTML cheatsheets and all six extracted ZIP packs as
a public Cloudflare Pages site, with a generated index. ZIP downloads are not
published. The personal interview page is intentionally public.

## Phases

1. Add a safe local sync command that builds `site/` from the supplied folder.
2. Verify the generated site, links, stale-file removal, and ZIP safety.
3. Commit and push the site, connect GitHub to Cloudflare Pages, and smoke test its URL.

## Dependencies and acceptance

- Source: `/home/tonythai93/Documents/cheatsheets`.
- Cloudflare Pages uses production branch `master`, build command `exit 0`, output directory `site`.
- Index links open all 11 cheatsheets; nested pages and images load; missing URLs return 404.
- The eight missing Go topic pages are reported as warnings and do not block publication.
- Updating the source, syncing, committing, and pushing updates the deployed site.
