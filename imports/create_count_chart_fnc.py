import matplotlib.pyplot as plt

def plot_column_distribution(
        df: pd.DataFrame,
        column_name: str,
        binsize: int = 10,
        chartsize: tuple[int, int] = (8, 3),
        title: Optional[str] = None
    ) -> None:
    """
    * Name:
    *    plot_column_distribution
    *
    * Code Complexity:
    *    simple
    *
    * Problem Statement:
    *    Visualizes the distribution of values within a specific column of a DataFrame, aiding in data exploration and analysis.
    *
    * Input:
    *    DataFrame, column name, optional binsize, chartsize, and title
    * Output:
    *    A histogram or bar plot showing the distribution of the specified column
    *
    * Description:
    *    Visualize data column distribution
    *
    * Parameters:
    *     df (pd.DataFrame): The DataFrame containing the data.
    *     column_name (str): The name of the column to plot.
    *     binsize (int, optional): The number of bins for the histogram, defaults to 10.
    *     chartsize (tuple, optional): Size of the output chart, defaults to (8, 3).
    *     title (str, optional): The title of the chart, defaults to None.
    *
    * Returns:
    *     None: Displays a plot but does not return a value.
    *
    * Example:
    *    Input: DataFrame containing 'Age', plot 'Age' column with binsize of 5
    *    Output: Histogram of 'Age' distribution with 5 bins
    *
    """
    # Validate column existence in DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    data = df[column_name].dropna()  # Remove missing values from the column

    # Set a default title if none is provided, adjusting for numerical data
    if not title:
        title = f'Distribution of {column_name}'
        if data.dtype != 'O' and binsize:  # Append binsize to title for numerical columns
            title += f' - Binsize {binsize}'

    # Determine plot type based on data type and uniqueness of values
    if data.dtype == 'O' or df[column_name].nunique() < binsize:  # For categorical data or numerical with few unique values
        value_counts = data.value_counts().head(binsize)  # Get top value counts up to binsize

        plt.figure(figsize=chartsize)
        value_counts.plot(kind='bar')  # Plot a bar chart
        plt.title(title)
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.xticks(rotation=45)

    else:  # For numerical data with sufficient unique values
        plt.figure(figsize=chartsize)
        plt.hist(data, bins=binsize, alpha=0.7, edgecolor='black')  # Plot a histogram
        plt.title(title)
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.grid(True)

    plt.show()  # Display the plot
