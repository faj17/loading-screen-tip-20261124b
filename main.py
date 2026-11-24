"""One-line loading-screen tip for the make.fun bounty.

The whole entry is a single tip aimed at stressed developers and the AI
coding agents working beside them: the agent already fixed the bug, and
the developer keeps breaking it again by endlessly "improving" the
prompt. The script validates the line and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The tip itself: one line, exactly 106 characters.
# Short on purpose: a loading-screen tip must land in a glance.
TIP = (
    "Tip: your AI fixed this bug three times already. "
    "Stop \u2018improving\u2019 the prompt \u2014 you\u2019re the one unfixing it."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the tip; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"tip must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("tip must be a single line")
    if not text.strip():
        raise ValueError("tip must not be only whitespace")
    return text


def main() -> None:
    text = validate(TIP)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
