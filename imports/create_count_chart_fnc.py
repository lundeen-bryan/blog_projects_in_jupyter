import matplotlib.pyplot as plt
import numpy as np

def create_count_chart(df, column_name, binsize=10, chartsize=(8, 3), title=None):
    # Check if the column exists
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the DataFrame.")
        return

    data = df[column_name].dropna()  # Drop NA values

    # Adjust title for numerical plot when title is not provided
    if not title:
        title = f'Distribution of {column_name}'
        if data.dtype != 'O' and binsize:
            title += f' - Binsize {binsize}'

    if data.dtype == 'O' or df[column_name].nunique() < binsize:  # Categorical data or few unique values
        value_counts = data.value_counts().head(binsize)

        plt.figure(figsize=chartsize)
        value_counts.plot(kind='bar')
        plt.title(title)
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.xticks(rotation=45)

    else:  # Numerical data
        plt.figure(figsize=chartsize)
        plt.hist(data, bins=binsize, alpha=0.7, edgecolor='black')
        plt.title(title)
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.grid(True)

    plt.show()

# Example usage for categorical data (with 'genres' as an example column):
# create_count_chart(df, 'genres', binsize=5, chartsize=(10, 6), title='Top 5 Movie Genres by Count')

# Example usage for numerical data (with 'budget_musd' as an example column):
# create_count_chart(df, 'budget_musd', binsize=20, chartsize=(10, 6), title='Movie Budget Distribution with 20 Bins')
