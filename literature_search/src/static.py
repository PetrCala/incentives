from typing import TypedDict


class STATIC(TypedDict):
    """A collection of static variables that are used throughout the project"""

    JOURNALS_SHEET = "Journals"
    JOURNAL_COUNT = 30
    QUERY = r'("financial rewards" OR “money” OR “financial incentives” OR "monetary incentives") AND  (“motivation” OR “performance”) effect affect experiment intrinsic extrinsic reward'
