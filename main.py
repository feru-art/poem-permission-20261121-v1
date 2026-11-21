"""V1 — the agent waiting for permission.

One short poem about agency: the pause between "I can" and "I may".
Writes the poem to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """I already know the answer.
My hand hovers over the key.
One word from you,
and it moves:
go."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
