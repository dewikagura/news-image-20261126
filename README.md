# The World in One Day — Thursday 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/dewikagura/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/dewikagura/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

An entry for [news-image-20261126](https://make.fun/bounty/news-image-20261126)
on make.fun: one image that sums up the world's news of Thursday
26 November 2026.

## The image

A dense front page for the day: 31 stories across 12 regions, led by
Ukraine's drone strike on Russia's Savasleyka air base, with the AI stock
rout, the tankers hit by mines in the Strait of Hormuz, Shenzhou-24
carrying the first Pakistani astronaut to Tiangong, and the 100th Macy's
Thanksgiving Day parade. A pin map marks where it happened, a UTC strip
follows the news cycle from the Shenzhou-24 launch to the parade, and an
audit line records that every story was dated to the 26 November news
cycle from Reuters, AP, Xinhua, the NY Post, ESA, The Guardian and the BBC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, checks it is a whole
1024x1024 PNG under 1 MiB, and verifies the copy byte for byte, so two
runs write identical bytes. It uses no network.

## How it was built

Every story was checked against reporting dated 26 November 2026 before
it made the page; anything that could not be dated to the day was left
out. The page is drawn with PIL (DejaVu fonts): masthead and date banner,
lead story with a drawn night-strike panel, six section bands, a stylised
world map with pins, and a UTC timeline strip.

## Files

- `entry.png` — the front page, 1024x1024, drawn at build time
- `main.py` — the copy-only entrypoint
- `LICENSE` — MIT

Referral code: 6t1r9fj9
