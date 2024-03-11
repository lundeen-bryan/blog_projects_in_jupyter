import pandas as pd

def null_values_sum(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the sum of null values per column and returns a dataframe with the results.

    Parameters:
    df (pd.DataFrame): The dataframe to calculate the null values for.

    Returns:
    pd.DataFrame: A dataframe with the column names, null values, and percentages of null values for each column. The percentage is formatted to 2 decimal places.
    """
    # Calculate the sum of null values per column
    null_sum = df.isnull().sum()
    # Calculate the percentage of null values per column
    null_percentage = (df.isnull().sum() / len(df)) * 100
    # Create a DataFrame to display the results
    null_df = pd.DataFrame({'Column': null_sum.index, 'Null Values': null_sum.values, 'Percentage': null_percentage.values})
    # Sort the DataFrame by the 'Percentage' column in descending order
    null_df = null_df.sort_values(by='Percentage', ascending=False)
    # Format the 'Percentage' column to make it more readable
    null_df['Percentage'] = null_df['Percentage'].apply(lambda x: f"{x:.2f}%")
    return null_df