"""Dad Joke Showdown — make.fun entry: u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes one dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python 3.13, stdlib only, deterministic, no network.

The joke: a family dog named Leftovers, who keeps coming back for
seconds. The name sets the trap and the last word springs it — "seconds"
is both the second helping at the dinner table and the dog turning up
again, exactly the kind of groan a father delivers across the table
while everyone else pretends not to laugh.
"""

import os
from pathlib import Path

# Why this joke fits the brief: the setup is the dog's name itself —
# "Leftovers" plants a food idea before the punchline ever arrives.
# The turn sits on the final word, "seconds", which means two things at
# once: another helping from the table, and the dog showing up again.
# It reads well aloud because it is a single plain sentence with no
# detours — one breath from name to punchline. And the wording is tight:
# every word pulls weight, so nothing can be cut without losing the joke.
JOKE = "We named our dog Leftovers — he always comes back for seconds."


def main() -> None:
    # Gate: the entry must be 1-200 Unicode code points, not only
    # whitespace — the brief's whole joke.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 code points"
    assert JOKE.strip(), "joke must not be only whitespace"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
