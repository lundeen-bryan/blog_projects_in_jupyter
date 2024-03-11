import pandas as pd

def unique_values_by_column(dataset: pd.DataFrame) -> pd.Series:
    """
    Returns a Series containing the number of unique values in each column of a DataFrame.

    Parameters
    ----------
    dataset : pd.DataFrame
        The input DataFrame.

    Returns
    -------
    pd.Series
        A Series containing the number of unique values in each column of the input DataFrame, sorted in descending order.

    Examples
    --------
    >>> import pandas as pd
    >>> from code_assistant import unique_values_by_column

    >>> df = pd.DataFrame({'A': [1, 2, 2, 3, 3], 'B': [4, 5, 5, 6, 6], 'C': [7, 8, 8, 9, 9]})
    >>> unique_values_by_column(df)
     A    2
     B    2
     C    2
    dtype: int64
    """
    unique_counts = dataset.nunique().sort_values(ascending=False)
    return unique_counts
