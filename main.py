import os
import time
import argparse
from scholar_wizard import search

QUERY = r'("financial rewards" OR “money” OR “financial incentives” OR "monetary incentives") AND  (“motivation” OR “performance”) effect affect experiment intrinsic extrinsic reward'
ARTIFACTS_DIR = os.path.join(
    os.path.dirname(__file__), "literature_search", "artifacts"
)
OUTPUT_DIR = os.path.join(ARTIFACTS_DIR, time.strftime("%Y%m%d"))

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Literature Search")
    parser.add_argument(
        "--search",
        help="Search Google Scholar for articles from all journals using the provided query.",
        action="store_true",
    )
    parser.add_argument(
        "--snowball", help="Run snowballing on the search results.", action="store_true"
    )
    args = parser.parse_args()

    if args.search:
        search(query=QUERY, output_path=OUTPUT_DIR, journals=None, use_proxy=False)
    elif args.snowball:
        print("Snowballing not implemented yet")
        pass
