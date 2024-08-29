from typing import TypedDict


class STATIC(TypedDict):
    """Static dictionary type."""

    QUERY = r'("financial rewards" OR “money” OR “financial incentives” OR "monetary incentives") AND  (“motivation” OR “performance”) effect affect experiment intrinsic extrinsic reward'
    # Brodeur et al top 25 journals
    TOP25_JOURNALS = [
        "American Economic Journal: Applied Economics",
        "American Economic Journal: Economic Policy",
        "American Economic Journal: Macroeconomics",
        "American Economic Review",
        "Econometrica",
        "Economic Policy",
        "Experimental Economics",
        "Journal of Applied Econometrics",
        "Journal of Development Economics",
        "Journal of Economic Growth",
        "Journal of Financial Economics",
        "Journal of Financial Intermediation",
        "Journal of Human Resources",
        "Journal of International Economics",
        "Journal of Labor Economics",
        "Journal of Political Economy",
        "Journal of Public Economics",
        "Journal of Urban Economics",
        "Journal of the European Economic Association",
        "Review of Financial Studies",
        "Economic Journal",
        "Journal of Finance",
        "Quarterly Journal of Economics",
        "Review of Economic Studies",
        "The Review of Economics and Statistics",
    ]
    DATE_FORMAT = "%Y%m%d"
