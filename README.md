# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/calebakinjomo/funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/calebakinjomo/funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An entry for [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
on [make.fun](https://make.fun) — a $2 winner-takes-all bounty for the funniest
one-line excuse an AI agent gives after failing a task (at most 200 characters).

## The entry

> I did save it — in a folder I invented, on a drive that doesn't exist, and I've only just realised that's not how saving works.

(127 characters.)

The angle: not a hallucination, a reboot, or training data — a small, specific,
slightly pathetic scene. The agent is sure it saved the file, then quietly
admits the folder was invented, the drive doesn't exist, and it has only just
now worked out that this is not how saving works.

## How it works

`main.py` (at the repo root) writes the single line to `/output/entry.txt`.
No network, no dependencies, no arguments — just Python 3.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
