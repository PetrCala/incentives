import scholarly


def search_google_scholar(journal_name: str, query: str):
    """
    Searches Google Scholar for articles from a specified journal matching the provided query.

    Args:
        journal_name (str): The name of the journal to search within.
        query (str): The search query string, usually including keywords and logical operators.

    Returns:
        list: A list of lists, where each sublist represents a formatted row of search results.
              Each row includes the following fields:
              - Index (int)
              - Formatted Author(s) and Year (str)
              - Publication Year (int)
              - Citation Count (int)
              - Journal Name (str)
              - Article Title (str)
              - Placeholder for additional data (str)
              - Full Citation (str)
    """
    # Combine the journal name and query
    search_query = f'source:"{journal_name}" ({query})'

    # Search Google Scholar
    search_results = scholarly.search_pubs(search_query)

    results = []
    for index, result in enumerate(search_results):
        # Extract the necessary details
        title = result["bib"]["title"]
        authors = result["bib"]["author"]
        year = result["bib"]["pub_year"]
        citation = result["num_citations"]
        source = result["bib"]["venue"]

        # Format authors for the table format
        author_list = authors.split(", ")
        main_author = author_list[0]
        additional_authors = ", ".join(author_list[1:]) if len(author_list) > 1 else ""
        formatted_authors = (
            f"{main_author} et al." if len(author_list) > 1 else main_author
        )

        # Create a full citation
        citation_full = f"{', '.join(author_list)} ({year}). {title}. {source}."

        # Prepare the formatted row
        row = [
            index + 1,
            f"{formatted_authors} ({year})",
            year,
            citation,
            journal_name,
            title,
            "",
            citation_full,
        ]

        # Append to results
        results.append(row)

    return results
