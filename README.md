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
{
  "by" : "dhouston",
  "descendants" : 71,
  "id" : 8863,
  "kids" : [ 8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 8940, 9067, 8908, 9055, 8865, 8881, 8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8870, 8980, 8934, 8876 ],
  "score" : 111,
  "time" : 1175714200,
  "title" : "My YC app: Dropbox - Throw away your USB drive",
  "type" : "story",
  "url" : "http://www.getdropbox.com/u/2/screencast.html"
}

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