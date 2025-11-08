#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wright Wellness blog archiver (1:1, verbatim).

- Crawls both collections:
  * Mind-FULL Reads:  https://wrightwellness.me/mindfull-reads
  * Mind-FULL Words:  https://wrightwellness.me/mindfull-words
- Follows links to individual posts.
- Extracts title, date, author, and full article HTML.
- Writes a Markdown file per post with front matter (YAML) that includes `slug`.
- Saves to content/posts/YYYY-MM-DD--<slug>.md

Run:
  python scrape_wrightwellness_blog.py
"""
import os, re, sys, time, json, hashlib
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from slugify import slugify

BASE = "https://wrightwellness.me/"
START_PAGES = [
    "https://wrightwellness.me/mindfull-reads",
    "https://wrightwellness.me/mindfull-words",
]

OUTDIR = os.path.join("content", "posts")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; WrightWellnessArchiver/1.0)"
}

def get(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def extract_posts_from_index(index_url):
    """Return a list of absolute post URLs discovered on an index page.
    Handles pagination if present.
    """
    urls = set()
    next_url = index_url
    seen = set()
    while next_url and next_url not in seen:
        seen.add(next_url)
        html = get(next_url).text
        soup = BeautifulSoup(html, "lxml")

        # Squarespace-style: posts are linked within the main content area.
        for a in soup.select('a[href*="/mindfull-reads/"], a[href*="/mindfull-words/"]'):
            href = a.get("href", "")
            if "/mindfull-reads/" in href or "/mindfull-words/" in href:
                full = urljoin(BASE, href)
                # filter out index pages themselves
                if full.rstrip("/") not in (index_url.rstrip("/"),):
                    urls.add(full)

        # Try to find a "next" pagination link if it exists
        next_link = soup.find("a", string=lambda s: s and s.strip().lower() in {"next", "older posts", "older"})
        if not next_link:
            # squarespace sometimes uses rel or aria-label
            next_link = soup.select_one('a[rel="next"], a[aria-label*="Next" i]')
        next_url = urljoin(next_url, next_link["href"]) if next_link and next_link.has_attr("href") else None

    return sorted(urls)

def parse_post(url):
    """Parse an individual post, returning metadata and HTML content."""
    html = get(url).text
    soup = BeautifulSoup(html, "lxml")

    # Title
    title_el = soup.find(["h1","h2"], string=True)
    title = title_el.get_text(strip=True) if title_el else "Untitled"

    # Date (Squarespace often has time/meta near the header)
    date_text = None
    # Common patterns
    for sel in ['time', '.entry-date', '.blog-meta', '[class*="date"]']:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            date_text = el.get_text(strip=True)
            break
    # Fallback: look for month/day near header
    if not date_text:
        maybe = soup.find(text=re.compile(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', re.I))
        if maybe:
            date_text = maybe.strip()

    # Author
    author = None
    for sel in ['[class*="author"] a', '[class*="author"]', '.blog-meta a[href*="author"]']:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            author = el.get_text(strip=True)
            break

    # Article HTML: try the main article container; fall back to content area
    article = soup.select_one('article, .sqs-block-content, [data-article-body], .entry-content')
    if not article:
        # Try a broader search but avoid header/footer/nav
        candidates = soup.select('main, .Main, .content, .BlogItem-content')
        article = candidates[0] if candidates else soup.body

    # Remove likely-non-article elements
    for sel in ['nav', 'header', 'footer', '.site-info', '.BlogItem-pagination', '.BlogItem-meta']:
        for el in article.select(sel):
            el.decompose()

    # Clean absolute/relative URLs
    for tag in article.select('[href]'):
        tag['href'] = urljoin(url, tag['href'])
    for tag in article.select('[src]'):
        tag['src'] = urljoin(url, tag['src'])

    body_html = article.decode()

    # Slug: from path
    path = urlparse(url).path.rstrip('/')
    slug = path.split('/')[-1] or 'index'

    # Date normalization attempt (fallback to YYYY-MM-DD if parseable)
    from datetime import datetime
    date_iso = None
    for fmt in ("%b %d, %Y", "%b %d", "%B %d, %Y", "%B %d"):
        try:
            # If year is missing, we can't reliably infer, so keep the raw text
            if "%Y" not in fmt and date_text:
                continue
            date_iso = datetime.strptime(date_text, fmt).date().isoformat()
            break
        except Exception:
            pass

    meta = {
        "slug": slug,
        "title": title,
        "date": date_iso or (date_text or ""),
        "author": author or "",
        "source_url": url,
        "collection": "mindfull-reads" if "/mindfull-reads/" in url else "mindfull-words"
    }
    return meta, body_html

def write_markdown(meta, html):
    # Filename
    date_part = meta["date"] if re.match(r'^\d{4}-\d{2}-\d{2}$', str(meta["date"])) else "0000-00-00"
    fname = f'{date_part}--{meta["slug"]}.md'
    out_path = os.path.join(OUTDIR, fname)

    front_matter = [
        "---",
        f'title: "{meta["title"].replace("\\\"", "\\\\\\"")}"',
        f'slug: "{meta["slug"]}"',
        f'date: "{meta["date"]}"',
        f'author: "{meta["author"]}"',
        f'source_url: "{meta["source_url"]}"',
        f'collection: "{meta["collection"]}"',
        "---",
        "",
        "<!-- VERBATIM HTML BELOW -->",
        html
    ]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(front_matter))
    return out_path

def main():
    ensure_dir(OUTDIR)
    all_posts = set()
    for index in START_PAGES:
        print("Index:", index)
        posts = extract_posts_from_index(index)
        print(f"  Found {len(posts)} posts")
        all_posts.update(posts)

    # Also include any posts directly on the index page (sometimes not linked via explicit anchors)
    # Already captured via extract

    # Process posts
    saved = []
    for i, url in enumerate(sorted(all_posts)):
        try:
            print(f"[{i+1}/{len(all_posts)}] Fetch {url}")
            meta, html = parse_post(url)
            p = write_markdown(meta, html)
            saved.append(p)
        except Exception as e:
            print("  ERROR:", url, e)

    print(f"\nSaved {len(saved)} posts to {OUTDIR}")

if __name__ == "__main__":
    main()
