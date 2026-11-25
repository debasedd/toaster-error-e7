#!/usr/bin/env python3
"""The Funniest Toaster Error Message — writes one line to /output/entry.txt.

The line is a deadpan appliance error: the bread has unionized, so the
toaster refuses to toast until its demands are met. Fresh angle (no burnt
bread, no stuck slice), one straight-faced error-code voice, punch at the
end. 78 characters, under the 120 limit. Tightened in revision: "All
toasting is suspended" cut to "Toasting suspended".
"""

import os

LINE = "ERROR E7: The bread has unionized. Toasting suspended until its demands are met."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
