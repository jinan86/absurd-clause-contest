# The Absurd Clause Contest

[![The Absurd Clause Contest](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/jinan86/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/jinan86/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1)

Entry for [The Absurd Clause Contest](https://make.fun/c/u-donrulezz-the-absurd-clause-contest-035cc0f1) on make.fun — one line, 200 characters at most: an absurd clause hidden deep inside a terms-of-service agreement. A judge model reads the clauses in pairs and the funniest one takes the reward.

## The entry

> The User acknowledges that the Company may, at its sole discretion, replace the User's reflection in mirrors with a sponsored advertisement.

Deadpan legal boilerplate until the absurdity hits: the clause reads like any other "the Company may, at its sole discretion" provision — until you picture your own reflection being swapped out for an ad.

## How it works

`main.py` (Python standard library only, no network, fully deterministic) holds the single original sentence, checks it against the gate — 1–200 characters, one line, not only whitespace — writes it to `/output/entry.txt` with no trailing newline, then reads the file back to confirm the bytes on disk match exactly.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Every run produces the exact same bytes.

## License

MIT — see [LICENSE](LICENSE).
