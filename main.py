import os
import time
import argparse
import scholar_wizard as sw
from incentives import STATIC as INCENTIVES_STATIC


ARTIFACTS_DIR = os.path.join(
    os.path.dirname(__file__), "literature_search", "artifacts"
)
OUTPUT_DIR = os.path.join(ARTIFACTS_DIR, time.strftime(INCENTIVES_STATIC.DATE_FORMAT))

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
        sw.search(
            query=INCENTIVES_STATIC.QUERY,
            output_path=OUTPUT_DIR,
            journals=INCENTIVES_STATIC.TOP25_JOURNALS,
            use_proxy=False,
        )
    elif args.snowball:
        print("Snowballing not implemented yet")
        pass
