from typing import TypedDict


class STATIC(TypedDict):
    """A collection of static variables that are used throughout the project"""

    JOURNALS_SHEET = "Journals"
    QUERY = r'("financial rewards" OR “money” OR “financial incentives” OR "monetary incentives") AND  (“motivation” OR “performance”) effect affect experiment intrinsic extrinsic reward'
    LIT_SEARCH_LOG_FILE = "literature_search.log"
