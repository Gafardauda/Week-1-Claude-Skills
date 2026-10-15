# examples/stats.py
# A deliberately WEAK module used to test the test-quality-review skill.
# It has code-quality smells and crashes on edge cases. Do not reuse it.


def calc(l):
    # Unclear name ("calc"), unclear parameter ("l").
    # Divides by len(l) with no guard: crashes on an empty list.
    s = 0
    for x in l:
        s = s + x
    return s / len(l)


def calc2(l):
    # Near-duplicate of calc() with one extra step (repetition / DRY smell).
    s = 0
    for x in l:
        s = s + x
    avg = s / len(l)
    return round(avg, 2)
