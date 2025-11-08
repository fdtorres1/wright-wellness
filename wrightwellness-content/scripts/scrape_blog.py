#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from slugify import slugify
from datetime import datetime

BASE = "https://wrightwellness.me/"
START_PAGES = [
    "https://wrightwellness.me/mindfull-reads",
    "https://wrightwellness.me/mindfull-words",
]
OUTDIR = os.path.join("content", "posts")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; WrightWellnessArchiver/1.0)"}

def get(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def extract_posts_from_index(index_url):
    urls = set()
    next_url = index_url
    seen = set()
    while next_url and next_url not in seen:
        seen.add(next_url)
        html = get(next_url).text
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select('a[href*="/mindfull-reads/"], a[href*="/mindfull-words/"]'):
            href = a.get("href", "")
            if "/mindfull-reads/" in href or "/mindfull-words/" in href:
                full = urljoin(BASE, href)
                if full.rstrip("/") not in (index_url.rstrip("/"),):
                    urls.add(full)
        next_link = (
            soup.find("a", string=lambda s: s and s.strip().lower() in {"next", "older posts", "older"})
            or soup.select_one('a[rel="next"], a[aria-label*="Next" i]')
        )
        next_url = urljoin(next_url, next_link["href"]) if next_link and next_link.has_attr("href") else None
    return sorted(urls)

def parse_post(url):
    html = get(url).text
    soup = BeautifulSoup(html, "lxml")
    title_el = soup.find(["h1","h2"], string=True)
    title = title_el.get_text(strip=True) if title_el else "Untitled"
    date_text = None
    for sel in ['time', '.entry-date', '.blog-meta', '[class*="date"]']:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            date_text = el.get_text(strip=True); break
    if not date_text:
        maybe = soup.find(text=re.compile(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', re.I))
        if maybe: date_text = maybe.strip()
    author = ""
    for sel in ['[class*="author"] a', '[class*="author"]', '.blog-meta a[href*="author"]']:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            author = el.get_text(strip=True); break
    article = soup.select_one('article, .sqs-block-content, [data-article-body], .entry-content') or soup.body
    for sel in ['nav', 'header', 'footer', '.site-info', '.BlogItem-pagination', '.BlogItem-meta']:
        for el in article.select(sel): el.decompose()
    for tag in article.select('[href]'): tag['href'] = urljoin(url, tag['href'])
    for tag in article.select('[src]'): tag['src'] = urljoin(url, tag['src'])
    body_html = article.decode()
    slug = (urlparse(url).path.rstrip('/').split('/')[-1] or 'index')
    date_iso = None
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d"):
        try:
            date_iso = datetime.strptime(date_text, fmt).date().isoformat(); break
        except Exception: pass
    meta = {
        "slug": slugify(slug),
        "title": title,
        "date": date_iso or (date_text or ""),
        "author": author,
        "source_url": url,
        "collection": "mindfull-reads" if "/mindfull-reads/" in url else "mindfull-words"
    }
    return meta, body_html

def write_markdown(meta, html):
    date_part = meta["date"] if re.match(r'^\\d{4}-\\d{2}-\\d{2}$', str(meta["date"])) else "0000-00-00"
    fname = f'{date_part}--{meta["slug"]}.md'
    out_path = os.path.join(OUTDIR, fname)
    front_matter = ["---",
        f'title: "{meta["title"].replace("\\\"", "\\\\\\"")}"',
        f'slug: "{meta["slug"]}"',
        f'date: "{meta["date"]}"',
        f'author: "{meta["author"]}"',
        f'source_url: "{meta["source_url"]}"',
        f'collection: "{meta["collection"]}"',
        "---", "", "<!-- VERBATIM HTML BELOW -->", html]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f: f.write("\\n".join(front_matter))
    return out_path

def main():
    ensure_dir(OUTDIR)
    all_posts = set()
    for index in START_PAGES:
        posts = extract_posts_from_index(index)
        all_posts.update(posts)
    for url in sorted(all_posts):
        try:
            meta, html = parse_post(url)
            write_markdown(meta, html)
        except Exception as e:
            print("ERROR:", url, e)

if __name__ == "__main__":
    main()
