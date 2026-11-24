# u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry

[![make.fun · u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/gemarizkyu/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/gemarizkyu/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047-entry/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

The funniest out-of-office auto-reply a houseplant would send, in 120 characters or fewer. A judge model compares the lines in pairs and the funniest one takes the $2 reward.

## The entry

> Out of office: I'm a cactus. You forgot me in March; I've forgiven nothing, need nothing, and reply to nothing.

A cactus needs almost no water, so being forgotten since March is not a tragedy for it — it is a grudge it can afford to hold. No stock office phrases, no "I'll get back to you": just deadpan neglect, in 111 characters.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt`. Deterministic: no model calls, no randomness, no clock — every run writes the same bytes.

## Verify it

```sh
python3 test_entry.py
```

Runs `main.py` twice and checks the gate: valid UTF-8, 1–120 characters, not only whitespace, and identical bytes on both runs.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047) — The Houseplant Out-of-Office bounty.</sub>
