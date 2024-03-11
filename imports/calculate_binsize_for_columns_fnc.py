import numpy as np
import pandas as pd

def calculate_binsize_for_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    * Name:
    *    calculate_optimal_bins
    *
    * Code Complexity:
    *    intermediate
    *
    * Problem Statement:
    *    Determines optimal bin sizes for histograms of numerical columns in a DataFrame, aiding in data visualization and analysis.
    *
    * Input:
    *    DataFrame with numerical and non-numerical columns
    * Output:
    *    DataFrame with columns names, bin sizes, and type (Continuous or Discrete)
    *
    * Description:
    *    Optimize bin sizes for histograms
    *
    * Parameters:
    *     df (pd.DataFrame): DataFrame with numerical columns for bin size calculation.
    *
    * Returns:
    *     pd.DataFrame: Contains columns 'Column', 'Bin Size', and 'Type'.
    *
    * Example:
    *    Input: DataFrame with 'Age' and 'Salary' columns
    *    Output: DataFrame with calculated bin sizes for 'Age' and 'Salary'
    *
    *    bin_size_fnc = load_function('calculate_binsize_for_columns_fnc', 'calculate_binsize_for_columns')
    *    if bin_size_fnc:
    *        binsize_df = bin_size_fnc(df)
    *        display(binsize_df)
    *    else:
    *        print('Sorry, could not calculate the bin size for the dataset.')
    *
    """
    bin_sizes = []  # List to store bin size information

    # Iterate through numerical columns to calculate bin sizes
    for column in df.select_dtypes(include=['float64', 'int64']):
        data = df[column].dropna()  # Remove missing values
        # Determine if the column is discrete or continuous based on unique value count
        if data.nunique() < 20:  # Discrete if less than 20 unique values
            bin_type = 'Discrete'
            bin_size = data.nunique()  # Use unique value count as bin size
        else:
            bin_type = 'Continuous'
            percentile_75, percentile_25 = np.percentile(data, [75, 25])  # Calculate 25th and 75th percentiles
            interquartile_range = percentile_75 - percentile_25  # Interquartile range
            bin_width = 2 * (interquartile_range) / (len(data) ** (1 / 3))  # Apply Freedman-Diaconis Rule
            bin_size = int((data.max() - data.min()) / bin_width)  # Calculate bin size
            bin_size = max(1, bin_size)  # Ensure at least 1 bin
        bin_sizes.append({'Column': column, 'Bin Size': bin_size, 'Type': bin_type})
    return pd.DataFrame(bin_sizes)

