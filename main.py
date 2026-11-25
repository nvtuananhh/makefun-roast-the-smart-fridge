"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Entry for make.fun bounty
``u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9``.

The program writes exactly one line — a roast of the smart fridge —
plus a trailing newline to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The line (79 characters, well inside the 160-character cap):

    My smart fridge keeps suggesting the salad I buried under three pizzas at 2 AM.

The joke: the fridge's "helpful" health nudges keep surfacing the one
virtuous thing in it, while politely ignoring the three pizzas piled on
top of it at 2 AM — a smart gadget that knows what you should eat and
still can't stop you eating what you actually want.

Python 3.13, standard library only, no network access.
"""

import os

ENTRY = "My smart fridge keeps suggesting the salad I buried under three pizzas at 2 AM."

# The gate requires 1-160 characters, a single line, not only whitespace.
assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} outside 1-160"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
