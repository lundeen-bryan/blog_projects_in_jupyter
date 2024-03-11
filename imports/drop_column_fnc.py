import pandas as pd

def drop_column(df, column_name):
    """
    Drop a specified column from a DataFrame and return the modified DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to modify.
    column_name : str
        The name of the column to drop.

    Returns
    -------
    pandas.DataFrame
        The modified DataFrame, with the specified column dropped.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'model_year': [1970, 1971], 'origin': ['USA', 'Japan'], 'name': ['ford pinto', 'toyota corolla']})
    >>> df = drop_column(df, 'name')  # Now, 'df' will be the DataFrame without the 'name' column.
    """
    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Drop the column and return the modified DataFrame
        return df.drop(columns=[column_name])
    else:
        print(f"The column '{column_name}' does not exist in the DataFrame.")
        # Return the original DataFrame unmodified
        return df
