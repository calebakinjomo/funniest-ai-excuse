#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives after failing a task,
spoken in the agent's own voice.

Angle: the agent confesses with total confidence — it invented the folder,
the drive, and the whole idea of saving, then realises none of it was real.
"""

import os

ENTRY = (
    "I did save it \u2014 in a folder I invented, on a drive that doesn't exist, "
    "and I've only just realised that's not how saving works."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
