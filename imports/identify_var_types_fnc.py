import pandas as pd
import pprint

def categorize_column_types(df: pd.DataFrame) -> None:
    """
    This function takes a pandas DataFrame as input and prints a dictionary
    with lists of numerical and categorical variables using pprint.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.

    Example usage:
        categorize_column_types(df)
    """
    # Identify numerical and categorical variables
    numerical_vars = df.select_dtypes(
        include=["int64", "float64", "int32", "float32"]
    ).columns.tolist()
    categorical_vars = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    # Print dictionary of variable types with numerical_vars first
    pprint.pprint({"numerical": numerical_vars, "categorical": categorical_vars})

# # Example usage
# categorize_column_types(df)

