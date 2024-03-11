import numpy as np
import matplotlib.pyplot as plt
import math

def plot_column_distributions(df, binsize_df, grid_title='Distribution of Values by Column - 10X scale'):
    """
    Generates a grid of distribution plots for specified columns in a DataFrame.

    Parameters:
    - df: DataFrame containing the data.
    - binsize_df: DataFrame containing 'Column' names and corresponding 'Bin Size'.
                  The actual bin size used in each chart is obtained by dividing the 'Bin Size' by 10 and rounding up,
                  to make the charts more interpretable at a reduced scale.
    - grid_title: String, optional title for the entire plot grid.

    Note:
    - The bin size scaling effectively reduces the granularity of the charts, making them simpler and emphasizing major trends.
    """
    columns = binsize_df['Column']
    n = len(columns)  # Number of plots

    # Determine the grid size (for simplicity, creating a square grid that fits all plots)
    grid_size = int(np.ceil(np.sqrt(n)))

    # Create the figure
    fig = plt.figure(figsize=(grid_size * 5, grid_size * 4))  # Adjust the figsize based on your preference

    # Add a main title to the figure
    fig.suptitle(grid_title, fontsize=16)

    for i, column in enumerate(columns, start=1):
        binsize_np = binsize_df.loc[binsize_df['Column'] == column, 'Bin Size'].values[0]
        binsize = math.ceil(binsize_np / 10)
        plt.subplot(grid_size, grid_size, i)  # Create subplot
        data = df[column].dropna()

        # Check data type and plot accordingly
        if data.dtype == 'O' or df[column].nunique() < binsize:
            value_counts = data.value_counts().head(binsize)
            value_counts.plot(kind='bar')
        else:
            plt.hist(data, bins=binsize, alpha=0.7, edgecolor='black')

        plt.title(column)
        plt.xticks(rotation=45)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust subplots to fit into the figure area, leaving space for the suptitle
    plt.show()

# Example usage
# plot_column_distributions(df, binsize_df, 'My Custom Title')
