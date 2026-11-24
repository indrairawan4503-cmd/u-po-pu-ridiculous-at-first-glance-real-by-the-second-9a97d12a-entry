"""Rent-a-Grandmother's Disapproval — one-sentence startup pitch.

Writes the pitch to /output/entry.txt (grader output) first, then
best-effort to entry.txt next to this file.
"""

import os

PITCH = "Rent-a-Grandmother books retired grandmothers by video to scold lonely adults for skipping meals, slouching, or staying single, and they pay per call because being nagged with love beats eating alone."


def main():
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 chars"
    assert PITCH.strip(), "pitch must not be only whitespace"
    assert PITCH == PITCH.strip(), "pitch must not have leading/trailing whitespace"
    assert "  " not in PITCH, "pitch must not contain double spaces"
    assert "\n" not in PITCH, "pitch must be a single line"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)

    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(PITCH)
    except OSError:
        pass

    print(f"chars: {len(PITCH)}")
    print(PITCH)


if __name__ == "__main__":
    main()
