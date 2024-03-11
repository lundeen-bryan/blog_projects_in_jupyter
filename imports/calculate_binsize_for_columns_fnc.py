import numpy as np
import pandas as pd


def calculate_binsize_for_columns(df):
    """
    Calculates the optimal bin size for each numerical column in a dataframe for the purpose
    of creating histograms. Utilizes the Freedman-Diaconis rule for continuous data
    and unique count for discrete data.

    Parameters:
    - df: Pandas DataFrame

    Returns:
    - A DataFrame with columns names, their determined bin sizes, and type (Continuous or Discrete)
    """
    bin_sizes = []

    for column in df.select_dtypes(include=['float64', 'int64']):
        data = df[column].dropna()
        if data.nunique() < 20:  # Considering it as discrete if unique values are less than 20
            bin_type = 'Discrete'
            bin_size = data.nunique()
        else:
            bin_type = 'Continuous'
            q75, q25 = np.percentile(data, [75, 25])
            iqr = q75 - q25
            bin_width = 2 * (iqr) / (len(data) ** (1 / 3))  # Freedman-Diaconis Rule
            bin_size = int((data.max() - data.min()) / bin_width)
            bin_size = max(1, bin_size)  # Ensuring at least 1 bin

        bin_sizes.append({'Column': column, 'Bin Size': bin_size, 'Type': bin_type})

    return pd.DataFrame(bin_sizes)

# Example usage with the movies_df dataset
# bin_size_df