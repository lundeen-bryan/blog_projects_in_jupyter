import pandas as pd

def is_mcar_random(mpg_df: pd.DataFrame) -> bool:
    """
    This function determines if the missing data in a given dataframe
    is missing completely at random (MCAR).

    Args:
        mpg_df (pd.DataFrame): The dataframe containing the data.

    Returns:
        bool: A boolean value indicating whether the data is MCAR or not.

    Examples:
        is_mcar = is_mcar_random(df)

        # If the data is MCAR, delete the missing values
        if is_mcar:
            df.dropna(subset=["column_with_missing_values"], inplace=True)
    """
    is_mcar = mpg_df.isnull().any().sum() == 0
    if is_mcar:
        print("The missing data is completely at random (MCAR).")
        del_rows = input("Do you want to delete the missing data? (y/n): ")
        if del_rows == "y":
            mpg_df.dropna(subset=["horsepower"], inplace=True)
    else:
        print("The missing data is not completely at random (not MCAR).")
        print("Consider other imputation methods.")
    return is_mcar
