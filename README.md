# Incentives

A revision of the Financial Incentives paper

## Literature search

- The literature search is based on the one ran during the bachelor thesis, upon which this research paper stands.
- We take the top 30 economic journals and search those using the following query:

  ```txt
  ("financial rewards" OR “money” OR “financial incentives” OR "monetary incentives") AND  (“motivation” OR “performance”) effect affect experiment intrinsic extrinsic reward
  ```

- The original list of journals has been lost, so we use a snapshot of the IDEAS/RePEc list from August 2020, which is the closest available snapshot to the original one, ran in July 2020. The August snapshot is available under the file `20_AUG_IDEAS:RePEc.html`.
- Using the top 30 journals, we scrape Google Scholar for studies using the python file `literature_search/search.py`. You can run this file by invoking the `run.sh` script like so:

  ```bash
  ./run.sh search
  ```

  This creates a new file in `literature_search/output` called `search_results.csv`.
