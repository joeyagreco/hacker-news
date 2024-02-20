<div align="center">
    <img src="https://raw.githubusercontent.com/joeyagreco/hacker-news/main/img/hacker_news.png" alt="hacker news logo" width="300"/>
<h1>Hacker News SDK</h1>
<h3>A Python Wrapper for the Hacker News API</h3>

[Hacker News API Documentation](https://github.com/HackerNews/API/blob/master/README.md)


<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.10-teal.svg"></a>
![Last Commit](https://img.shields.io/github/last-commit/joeyagreco/hacker-news)
<br>
![E2E Tests](https://github.com/joeyagreco/hacker-news/actions/workflows/e2e-tests.yml/badge.svg)
![Build](https://github.com/joeyagreco/hacker-news/actions/workflows/build.yml/badge.svg)
![Formatting Check](https://github.com/joeyagreco/hacker-news/actions/workflows/formatting-check.yml/badge.svg)
</div>

## Quickstart

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install hn-sdk
```

### Get an Item by ID
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(8863))
```
```sh
```

## Development

### Install Dependencies
```sh
make deps
```

### Run E2E Tests
```sh
make test-e2e
```

### Format Code
```sh
make fmt
```