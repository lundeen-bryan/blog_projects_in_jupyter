import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_density_graphs(dataframe: pd.DataFrame):
    """
    Generate density plots for numerical variables in a DataFrame using a histplot with KDE overlaid.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame containing numerical variables.

    Returns:
    None

    Examples:
        # Load the data into a pandas dataframe
        df = pd.read_csv("data.csv")

        # Use the plot_density_graphs function
        plot_density_graphs(df)
    """
    # Get list of numerical columns excluding those already analyzed and 'name'
    numerical_columns = [col for col in dataframe.select_dtypes(include='number').columns
                         if col not in ['cylinders', 'origin', 'model_year', 'name']]

    # Loop through each numerical variable
    for variable in numerical_columns:
        plt.figure(figsize=(8, 6))

        # Create histplot with KDE overlaid
        sns.histplot(data=dataframe, x=variable, kde=True, color='skyblue')

        # Add labels and title
        plt.xlabel(variable.capitalize())
        plt.ylabel('Frequency / Density')
        plt.title(f'Density Plot of {variable.capitalize()}')

        # Show plot
        plt.show()

