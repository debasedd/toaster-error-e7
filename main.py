#!/usr/bin/env python3
"""The Funniest Toaster Error Message — writes one line to /output/entry.txt.

The line is a deadpan error from a kitchen toaster that resents its job:
the bread is lodged sideways, and the toaster points out it never went to
culinary school for this. Real error format (code + fault), one voice all
the way through, no bread pun — the surprise is the appliance's career
grievance, not the toast.
"""

import os

LINE = "E-07: Bread lodged sideways. I did not go to culinary school for this."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
