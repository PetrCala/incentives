import os
from loguru import logger
import pandas as pd
from src import PATHS, STATIC, config
from src.file_handling import load_src_file, save_output
from src.scholar import search_google_scholar


def main():
    logger.info("Initializing the literature search")

    df = load_src_file()
    merged_results = pd.DataFrame()
    idx = 0

    logger.info("Starting literature search")

    for i, study in df.iterrows():
        logger.info(f"Processing journal {study["Journal"]}")
        search_results: pd.DataFrame = search_google_scholar(
          journal_name=study["Search Keyword"], 
          query=STATIC.QUERY,
          idx = idx,
          save_results_to_pdf=config.SAVE_RESULS_TO_PDF
        )
        merged_results = pd.concat([merged_results, search_results], ignore_index=True)
        idx += search_results.shape[0]


    save_output(merged_results)

    logger.success("Literature search completed")


if __name__ == "__main__":
    logger.debug(f"Changing directory to {PATHS.RUN_DIR}")
    os.chdir(PATHS.RUN_DIR)

    main()
