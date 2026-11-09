"""Synthetic test file for the Claude-Codex bridge pilot. Not real code."""


def average(values):
    """Return the mean of a list of numbers."""
    total = 0
    for v in values:
        total += v
    return total / len(values)  # fails on an empty list


if __name__ == "__main__":
    print(average([1, 2, 3]))
    print(average([]))
