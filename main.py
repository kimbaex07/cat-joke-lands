"""One-line cat joke entry for make.fun.

Writes the single joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python stdlib, deterministic, no network.
"""

import os

LINE = "My cat finally caught the laser dot, froze, and stared at me like I'd been lying to him for years."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
