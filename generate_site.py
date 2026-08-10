#!/usr/bin/env python3
"""
Static site generator for the blog.

Reads post content from posts_data.py, renders it through the Jinja2
templates in templates/, and writes plain HTML files that GitHub Pages
can serve directly (no server-side Python involved at deploy time).

Usage:
    pip install -r requirements.txt
    python generate_site.py

Output:
    index.html          <- blog list page
    posts/<slug>.html   <- one file per post
    static/style.css    <- copied from static/style.css (source of truth)
"""

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from posts_data import POSTS

ROOT_DIR = Path(__file__).parent
TEMPLATES_DIR = ROOT_DIR / "templates"
OUTPUT_DIR = ROOT_DIR  # write straight to the repo root, same as before
POSTS_OUTPUT_DIR = OUTPUT_DIR / "posts"


def build():
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))

    POSTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Sort newest first by date, in case posts_data.py isn't kept in order.
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)

    # --- Blog list page (index.html) ---
    index_template = env.get_template("index.html")
    index_html = index_template.render(
        page_title="Blog",
        meta_description="Personal essays, career and tech notes, and the slow build of Freiya Studio.",
        root="",
        posts=posts,
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("wrote index.html")

    # --- Individual post pages (posts/<slug>.html) ---
    post_template = env.get_template("post.html")
    for post in posts:
        post_html = post_template.render(
            page_title=post["title"],
            meta_description=post["dek"],
            root="../",
            post=post,
        )
        out_path = POSTS_OUTPUT_DIR / f"{post['slug']}.html"
        out_path.write_text(post_html, encoding="utf-8")
        print(f"wrote posts/{post['slug']}.html")

    # .nojekyll tells GitHub Pages to serve the files as-is, no Jekyll build.
    (OUTPUT_DIR / ".nojekyll").touch()


if __name__ == "__main__":
    build()
