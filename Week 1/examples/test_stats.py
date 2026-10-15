# examples/test_stats.py
# A deliberately THIN test used to test the test-quality-review skill.
# It only checks the happy path and misses the risky edge cases.

from stats import calc


def test_calc_average():
    # Happy path only: a normal list of numbers.
    assert calc([10, 20, 30]) == 20

# Missing on purpose (what a good review should flag):
# - empty list []        -> currently crashes (divide by zero)
# - negative numbers
# - a single value
# - no tests at all for calc2()
