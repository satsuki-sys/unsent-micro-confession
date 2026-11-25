#!/usr/bin/env python3
"""Entry for make.fun "Unsent: The Micro-Confession Sprint"
(u-boothlord-unsent-the-micro-confession-sprint-8c6596ba).

Writes one two-part micro-confession — a To: line and the unsent message
itself, exactly as typed — to /output/entry.txt. Stdlib only, no network.

The confession: a younger sibling's apology that stayed in drafts because
it is too honest to send — laughing at a brother being yelled at, and
admitting the relief that it wasn't them.

Revised entry (v2): "that night" was vague and could fit any sibling
fight, so the scene is anchored in the kitchen — a shared-household
memory only this brother shares, which makes the To: line and the
message need each other. The lowercase typing is kept so it reads as
typed, never sent.
"""

import os

ENTRY = (
    "To: my older brother\n"
    "i'm sorry i laughed when dad yelled at you in the kitchen that night. "
    "i was just glad it wasn't me"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
