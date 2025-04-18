# Yesterday CLI

`yesterday` is a tiny Python CLI tool that tells you what day was yesterday. Nothing more. Nothing less.

It handles all the hard work of going back in time by exactly one day — so you don’t have to.

Built with zero dependencies, just pure Python and a mild sense of humor.

## Tutorial

- Medium: [Publish Your Python Package to PyPI](https://blog.ilyakhrustalev.com/publish-your-python-package-to-pypi-using-github-actions-in-2025-7def5fb989c8)

## Branches

- [steps/1-boilerplate](https://github.com/rznzippy/yesterday_cli/tree/steps/1-boilerplate) – Basic project boilerplate
- [steps/2-add-uv](https://github.com/rznzippy/yesterday_cli/tree/steps/2-add-uv) – Added `uv` for packaging and dependency management
- [steps/3-publish-config](https://github.com/rznzippy/yesterday_cli/tree/steps/3-publish-config) – Added PyPI publishing configuration
- [steps/4-automatic-versioning](https://github.com/rznzippy/yesterday_cli/tree/steps/4-automatic-versioning) – Enabled automatic versioning
- [steps/5-github-action](https://github.com/rznzippy/yesterday_cli/tree/steps/5-github-action) – Set up GitHub Action for automated publishing

## Usage

```bash
$ yesterday --help

usage: yesterday [-h] [-d] [-q]

Tell you what day was yesterday.

options:
  -h, --help     show this help message and exit
  -d, --date     print yesterday's full date
  -q, --quiet    just output the date, no text
```

### Examples

```bash
$ yesterday
Yesterday was Friday.

$ yesterday --date
Yesterday was 2025-04-11.

$ yesterday --quiet --date
2025-04-11
```
