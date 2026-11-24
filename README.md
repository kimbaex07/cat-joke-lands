# The One-Line Cat Joke That Lands

![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)
![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)
![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)

A one-line cat joke, written fresh from scratch for the make.fun contest
**"The One-Line Cat Joke That Lands"** (`u-aldy998-the-one-line-cat-joke-that-lands-a7b18262`,
prize $2, deadline 26 Nov 2026 15:40 UTC).

## The joke

> My cat finally caught the laser dot, froze, and stared at me like I'd been lying to him for years.

**Character count:** 98 (limit: under 200 characters — 102 chars of headroom)

Why it lands: the setup is the familiar laser-pointer chase every cat
owner knows; the turn flips the joke onto the owner — the cat doesn't
celebrate the catch, he realises he's been tricked for years. No pun,
no padding, no explanation after the punchline, and easy to retell.

## What it does

`main.py` writes the joke line — and nothing else — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Pure Python
standard library only, deterministic, no network access, no secrets.

## How to run

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

Verified locally: `out/entry.txt` holds exactly one line, 98 characters,
byte-for-byte identical to the line quoted above. `entry.txt` is generated
at grading time and is not committed.

## License

MIT — see [LICENSE](LICENSE).
