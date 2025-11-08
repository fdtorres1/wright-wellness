# Wright Wellness — Content + Verbatim Blog Archive

This repository combines:
- **/content/pages** — Markdown copies of Wright Wellness core pages (with front matter).
- **/content/posts** — Destination for *verbatim* blog posts (Mind-FULL Reads & Words). Placeholders included now; run the scraper to fetch full HTML.
- **/scripts/scrape_blog.py** — A Python script to archive every post 1:1 and save to `/content/posts/`.
- **requirements.txt** — Dependencies for the scraper.

## Usage

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/scrape_blog.py
```

Archived posts will be saved as `YYYY-MM-DD--<slug>.md` with front matter:
`title, slug, date, author, source_url, collection` and the **verbatim HTML body** embedded below.

> Note: Long page bodies on /content/pages are summarized for now. Replace or expand as needed during redesign.
