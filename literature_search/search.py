import os
from loguru import logger
import pandas as pd
from src import PATHS, STATIC
from src.file_handling import load_src_file, save_output
from src.scholar import search_google_scholar


def main():
    logger.info("Initializing the literature search")

    df = load_src_file()
    out_df = pd.DataFrame()

    logger.info("Starting literature search")

    for i, study in df.iterrows():
        study_name = study["Journal"]
        logger.info(f"Processing journal {study_name}")
        result = search_google_scholar(journal_name=study_name, query=STATIC.QUERY)
        out_df = out_df.append(result)

    save_output(out_df)

    logger.success("Literature search completed")


if __name__ == "__main__":
    logger.debug(f"Changing directory to {PATHS.RUN_DIR}")
    os.chdir(PATHS.RUN_DIR)

    main()
