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

#### Story
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(8863))
```
```sh
{
  "by" : "dhouston",
  "descendants" : 71,
  "id" : 8863,
  "kids" : [ 8952, 9224, 8917, 8884, ..., 8876 ],
  "score" : 111,
  "time" : 1175714200,
  "title" : "My YC app: Dropbox - Throw away your USB drive",
  "type" : "story",
  "url" : "http://www.getdropbox.com/u/2/screencast.html"
}
```

#### Comment
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(2921983))
```
```sh
{
  "by" : "norvig",
  "id" : 2921983,
  "kids" : [ 2922097, 2922429, 2924562, 2922709, ..., 2922141 ],
  "parent" : 2921506,
  "text" : "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?",
  "time" : 1314211127,
  "type" : "comment"
}
```

#### Ask
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(121003))
```
```sh
{
  "by" : "tel",
  "descendants" : 16,
  "id" : 121003,
  "kids" : [ 121016, 121109, 121168 ],
  "score" : 25,
  "text" : "<i>or</i> HN: the Next Iteration<p>I get the impression that with Arc being released a lot of people who never had time for HN before are suddenly dropping in more often. (PG: what are the numbers on this? I'm envisioning a spike.)<p>Not to say that isn't great, but I'm wary of Diggification. Between links comparing programming to sex and a flurry of gratuitous, ostentatious  adjectives in the headlines it's a bit concerning.<p>80% of the stuff that makes the front page is still pretty awesome, but what's in place to keep the signal/noise ratio high? Does the HN model still work as the community scales? What's in store for (++ HN)?",
  "time" : 1203647620,
  "title" : "Ask HN: The Arc Effect",
  "type" : "story"
}
```

#### Job
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(121003))
```
```sh
{
  "by" : "justin",
  "id" : 192327,
  "score" : 6,
  "text" : "Justin.tv is the biggest live video site online. We serve hundreds of thousands of video streams a day, and have supported up to 50k live concurrent viewers. Our site is growing every week, and we just added a 10 gbps line to our colo. Our unique visitors are up 900% since January.<p>There are a lot of pieces that fit together to make Justin.tv work: our video cluster, IRC server, our web app, and our monitoring and search services, to name a few. A lot of our website is dependent on Flash, and we're looking for talented Flash Engineers who know AS2 and AS3 very well who want to be leaders in the development of our Flash.<p>Responsibilities<p><pre><code>    * Contribute to product design and implementation discussions\n    * Implement projects from the idea phase to production\n    * Test and iterate code before and after production release \n</code></pre>\nQualifications<p><pre><code>    * You should know AS2, AS3, and maybe a little be of Flex.\n    * Experience building web applications.\n    * A strong desire to work on website with passionate users and ideas for how to improve it.\n    * Experience hacking video streams, python, Twisted or rails all a plus.\n</code></pre>\nWhile we're growing rapidly, Justin.tv is still a small, technology focused company, built by hackers for hackers. Seven of our ten person team are engineers or designers. We believe in rapid development, and push out new code releases every week. We're based in a beautiful office in the SOMA district of SF, one block from the caltrain station. If you want a fun job hacking on code that will touch a lot of people, JTV is for you.<p>Note: You must be physically present in SF to work for JTV. Completing the technical problem at <a href=\"http://www.justin.tv/problems/bml\" rel=\"nofollow\">http://www.justin.tv/problems/bml</a> will go a long way with us. Cheers!",
  "time" : 1210981217,
  "title" : "Justin.tv is looking for a Lead Flash Engineer!",
  "type" : "job",
  "url" : ""
}
```

#### Poll
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(126809))
```
```sh
{
  "by" : "pg",
  "descendants" : 54,
  "id" : 126809,
  "kids" : [ 126822, 126823, 126993, 126824, ..., 126875 ],
  "parts" : [ 126810, 126811, 126812 ],
  "score" : 46,
  "text" : "",
  "time" : 1204403652,
  "title" : "Poll: What would happen if News.YC had explicit support for polls?",
  "type" : "poll"
}
```

#### Part of Another Item
```python
from hn_sdk.client.v0.client import get_item_by_id

print(get_item_by_id(160705))
```
```sh
{
  "by" : "pg",
  "id" : 160705,
  "poll" : 160704,
  "score" : 335,
  "text" : "Yes, ban them; I'm tired of seeing Valleywag stories on News.YC.",
  "time" : 1207886576,
  "type" : "pollopt"
}
```
---
### Get a User by Username

```python
from hn_sdk.client.v0.client import get_user_by_username

print(get_user_by_username("joeyagreco"))
```
```sh
{
    "created": 1663896930,
    "id": "joeyagreco",
    "karma": 4,
    "submitted": [38474886, 35729377, 35729231, 32946977, 32946976],
}
```
---
### Get Current Largest Item ID
```python
from hn_sdk.client.v0.client import get_max_item_id

print(get_max_item_id())
```
```sh
39438426
```
---
### Get New Stories
```python
from hn_sdk.client.v0.client import get_new_stories

print(get_new_stories())
```
```sh
[ 39431573, 39431552, 39431514, 39431505, ..., 39432231 ]
```
---
### Get Top Stories
```python
from hn_sdk.client.v0.client import get_top_stories

print(get_top_stories())
```
```sh
[ 39396571, 39385098, 39387191, 39389092, ..., 39394528 ]
```
---
### Get Best Stories
```python
from hn_sdk.client.v0.client import get_best_stories

print(get_best_stories())
```
```sh
[ 39437424, 39418810, 39418102, 39422238, ..., 39402906 ]
```
---
### Get Ask HN Stories
```python
from hn_sdk.client.v0.client import get_ask_stories

print(get_ask_stories())
```
```sh
[ 39405805, 39405655, 39400290, 39398791,  ..., 39427773 ]
```
---
### Get Show HN Stories
```python
from hn_sdk.client.v0.client import get_show_stories

print(get_show_stories())
```
```sh
[ 39387382, 39403234, 39410058, 39391731,  ..., 39390544 ]
```
---
### Get Job Stories
```python
from hn_sdk.client.v0.client import get_job_stories

print(get_job_stories())
```
```sh
[ 39057748, 39040718, 39038845, 39019063,  ..., 39006337 ]
```
---
### Get Changed Items and Profiles
```python
from hn_sdk.client.v0.client import get_updates

print(get_updates())
```
```sh
{
  "items" : [ 8423305, 8420805, 8423379, 8422504, ..., 8422087 ],
  "profiles" : [ "thefox", "mdda", "plinkplonk", "GBond", ..., "Bogdanp" ]
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