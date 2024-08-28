import os
from loguru import logger
import pandas as pd


BASE_DIR = "literature_search"  # Where the script is located
OUTPUT_FOLDER = "output"
RUN_DIR = os.path.abspath(os.path.dirname(__file__))  # Where the script is executed

SRC_FILE = os.path.join(RUN_DIR, "LoS_incentives_revision_micro.xlsx")
OUTPUT_FILE = os.path.join(RUN_DIR, OUTPUT_FOLDER, "search.csv")
JOURNALS_SHEET = "Journals"


def load_src_file() -> pd.DataFrame:
    logger.debug("Loading source file")
    assert os.path.exists(SRC_FILE), f"File {SRC_FILE} not found"

    try:
        df = pd.read_excel(SRC_FILE, sheet_name=JOURNALS_SHEET)
        breakpoint()
        return df
    except Exception as e:
        logger.error(f"Error loading source file: {e}")
        raise e


def main():
    logger.info("Initializing the literature search")

    df = load_src_file()

    logger.success("Literature search completed")


if __name__ == "__main__":
    logger.debug(f"Changing directory to {RUN_DIR}")
    os.chdir(RUN_DIR)

    main()
