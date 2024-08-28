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


def save_output(out_df: pd.DataFrame):
    """Save the output data frame to a CSV file."""
    logger.debug(f"Saving output file to {PATHS.OUTPUT_FILE}")
    if not os.path.exists(PATHS.OUTPUT_DIR):
        os.makedirs(PATHS.OUTPUT_DIR)
    out_df.to_csv(PATHS.OUTPUT_FILE, index=False)
