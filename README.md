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
| Research overview and project cards | `research.md` (images in `assets/img/research/`) |
| Publications                       | `_data/publications.yml`               |
| CV                                 | replace `assets/pdf/cv.pdf`            |
| Colors, fonts, spacing             | `assets/css/style.css` (variables at the top) |
| Page structure (header, footer)    | `_layouts/` and `_includes/`           |

## Publishing

Pushing to `master` runs the workflow in `.github/workflows/jekyll.yml`, which builds the site
and publishes it (repo Settings → Pages → Source must be "GitHub Actions").
Progress and errors show in the repo's **Actions** tab.

## Credits

Font: [Inter](https://rsms.me/inter/) (SIL Open Font License, see `assets/fonts/OFL.txt`).
Brand icons from [Simple Icons](https://simpleicons.org/) (CC0).
