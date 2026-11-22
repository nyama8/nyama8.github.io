# nyama8.github.io

Personal academic website of Nicholas S. Yama, built with [Jekyll](https://jekyllrb.com/)
and published by GitHub Pages at <https://nyama8.github.io>.

## Preview locally

One-time setup: Homebrew Ruby (`brew install ruby`, with `/opt/homebrew/opt/ruby/bin` on your PATH),
then in this folder:

```bash
bundle install
```

Each time:

```bash
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>. Pages reload as you save files
(restart the command after editing `_config.yml`). Stop it with Ctrl+C.

## Where things are

| To change…                         | Edit                                   |
|------------------------------------|----------------------------------------|
| Bio (About page)                   | `index.md`                             |
| Name, position, email, links       | `_config.yml`                          |
| Professional training, awards (About page) | `_data/training.yml`, `_data/awards.yml` |
| Research intro text | `research.md` |
| Research topics (cards + their own pages) | one file per topic in `_topics/` (images in `assets/img/research/`) |
| Publications                       | `_data/publications.yml`               |
| CV                                 | replace `assets/pdf/cv.pdf`            |
| Colors, fonts, spacing             | `assets/css/style.css` (variables at the top) |
| Page structure (header, footer)    | `_layouts/` and `_includes/`           |

## Optional background (off)

There is a faint network decoration (nodes and links, pinned to the bottom of the window)
that is switched off. To turn it on, set `background_network: true` in `_config.yml` and
restart the preview. The drawing is made by a small Python script; to change it (density,
shape, colors, a different random layout via `SEED`), edit the settings at the top of
`_scripts/make-network.py` and run, from this folder:

```
python3 _scripts/make-network.py
```

It rewrites `assets/img/network-light.svg` and `assets/img/network-dark.svg`. If the browser
still shows the old drawing, reload with Cmd+Shift+R.

## Publishing

Pushing to `master` runs the workflow in `.github/workflows/jekyll.yml`, which builds the site
and publishes it (repo Settings → Pages → Source must be "GitHub Actions").
Progress and errors show in the repo's **Actions** tab.

## Credits

Font: [Inter](https://rsms.me/inter/) (SIL Open Font License, see `assets/fonts/OFL.txt`).
Brand icons from [Simple Icons](https://simpleicons.org/) (CC0).
