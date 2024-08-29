import os
import time
from loguru import logger
import pandas as pd
from src import PATHS, STATIC, config
from src.file_handling import load_src_file, save_output
from src.scholar import search_google_scholar, use_proxy
from src.utils import save_metadata

# Clear the literature search log file upon each script execution
with open(PATHS.LIT_SEARCH_LOG_FILE, 'w'):
    pass

def main():
    logger.add(PATHS.LIT_SEARCH_LOG_FILE, rotation="10 MB", backtrace=True, diagnose=True)
    logger.info("Initializing the literature search")

    df = load_src_file()
    merged_results = pd.DataFrame()
    idx = 0

    use_proxy()

    logger.info("Starting literature search")

    for i, study in df.iterrows():
        logger.info(f"Processing journal {study["Journal"]} ({i+1}/{config.JOURNAL_COUNT})")
        search_results: pd.DataFrame = search_google_scholar(
          journal_name=study["Search Keyword"], 
          query=STATIC.QUERY,
          idx = idx,
          save_results_to_pdf=config.SAVE_RESULS_TO_PDF
        )
        merged_results = pd.concat([merged_results, search_results], ignore_index=True)
        idx += search_results.shape[0]


    file_suffix= time.strftime("%Y%m%d-%H%M%S")
    save_output(merged_results, file_suffix=file_suffix)
    save_metadata(merged_results, file_suffix=file_suffix)

    logger.success("Literature search completed")


if __name__ == "__main__":
    logger.debug(f"Changing directory to {PATHS.RUN_DIR}")
    os.chdir(PATHS.RUN_DIR)

    main()
