# blog

Source for [freillamae13.github.io/blog](https://freillamae13.github.io/blog/), built with a small Python script instead of a framework.

## How it works

- `posts_data.py` holds the content for every post (title, tags, date, body).
- `templates/` holds the Jinja2 HTML templates (shared header/footer, post layout, list layout).
- `static/style.css` holds all the styling.
- `generate_site.py` reads the posts, runs them through the templates, and writes plain HTML:
  - `index.html`, the blog list page
  - `posts/<slug>.html`, one file per post

GitHub Pages just serves the generated HTML. There's no server-side Python at runtime, the Python only runs when you build the site.

## Add a new post

1. Open `posts_data.py` and copy one of the entries in `POSTS`.
2. Give it a new `slug` (this becomes the filename, e.g. `posts/my-new-post.html`).
3. Fill in `title`, `dek`, `tags`, `date`, `author`, and `body_html`.
4. Run the build:

   ```bash
   pip install -r requirements.txt
   python generate_site.py
   ```

5. Commit and push. `index.html` and `posts/*.html` are regular files checked into the repo, so pushing them is what updates the live site.

If you'd rather not run the build locally every time, `.github/workflows/build.yml` rebuilds and commits the site automatically whenever `posts_data.py`, `templates/`, or `static/` change on `main`.

## Deploying

GitHub Pages settings for this repo: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`**.

This build uses the default GitHub Pages URL, `freillamae13.github.io/blog`, no custom domain. If a `CNAME` file exists in the repo (left over from a previous setup), delete it:

```bash
git rm CNAME
```

Then in **Settings → Pages → Custom domain**, clear the field and click Save, and remove the DNS records at your domain registrar if you had added any for `iamella.com`.