import os
from loguru import logger
import pandas as pd
from src import PATHS, STATIC


def load_src_file() -> pd.DataFrame:
    """Load the source excel file with the studies and return it as a DataFrame."""
    logger.debug("Loading source file")
    assert os.path.exists(PATHS.SRC_FILE), f"File {PATHS.SRC_FILE} not found"

    try:
        df = pd.read_excel(PATHS.SRC_FILE, sheet_name=STATIC.JOURNALS_SHEET)
        assert (
            df.shape[0] == STATIC.JOURNAL_COUNT
        ), f"Expected {STATIC.JOURNAL_COUNT} journals, found {df.shape[0]}"
        return df
    except Exception as e:
        logger.error(f"Error loading source file: {e}")
        raise e


def process_journal(study: pd.Series) -> pd.DataFrame:
    """Process a single journal, query it for studies, and return the data frame that can be appended to the output one."""

    pass


def save_output(out_df: pd.DataFrame):
    """Save the output data frame to a CSV file."""
    logger.debug(f"Saving output file to {PATHS.OUTPUT_FILE}")
    if not os.path.exists(PATHS.OUTPUT_DIR):
        os.makedirs(PATHS.OUTPUT_DIR)
    out_df.to_csv(PATHS.OUTPUT_FILE, index=False)


def main():
    logger.info("Initializing the literature search")

    df = load_src_file()
    out_df = pd.DataFrame()

    logger.info("Starting literature search")

    for i, study in df.iterrows():
        logger.info(f"Processing journal {study['Journal']}")
        result = process_journal(study)
        out_df = out_df.append(result)

    save_output(out_df)

    logger.success("Literature search completed")


if __name__ == "__main__":
    logger.debug(f"Changing directory to {PATHS.RUN_DIR}")
    os.chdir(PATHS.RUN_DIR)

    main()
