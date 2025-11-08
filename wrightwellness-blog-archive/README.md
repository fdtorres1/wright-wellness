# Wright Wellness — Full Blog Archive (1:1)

This repo scaffolds a **verbatim** export of all Wright Wellness blog posts (Mind-FULL Reads and Mind-FULL Words).

## What's included

- `scrape_wrightwellness_blog.py` — a Python 3 script you can run **locally** to fetch the entire archive.
- `content/posts/` — destination for Markdown files with front matter and full HTML body preserved.
- Front matter includes: `slug`, `title`, `date`, `author`, `source_url`, `collection`.

> Note: This workspace cannot access the public web, so the script isn't executed here. Run it on your machine.

## Usage

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scrape_wrightwellness_blog.py
```

Results will be written to `content/posts/`.

## File naming

Files are saved as `YYYY-MM-DD--<slug>.md`. The `slug` is derived from the original URL path.
