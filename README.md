# PhDOps

## Local development

Install [uv](https://docs.astral.sh/uv/) and use Python 3.11 or newer.

```sh
git submodule update --init --recursive
uv sync
uv run pelican content -s pelicanconf.py
uv run pelican --listen
```

Open http://localhost:8000 to preview the generated site.

The `pelican-bootstrap3` submodule uses Git over SSH and is pinned to
`e431257`, the last commit before the original repository removed the theme
and redirected users to `getpelican/pelican-themes`. Updating to the original
repository's latest commit will remove the theme files.
