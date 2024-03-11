import pandas as pd
import xlwings as xw


def dtypes_to_excel(df: pd.DataFrame, sheet_name: str = 'Data Types') -> None:
    """
    Export the data types of a Pandas DataFrame to an Excel sheet.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to export.
    sheet_name : str, optional
        The name of the Excel sheet to create, by default 'Data Types'.

    Returns
    -------
    None
        This function does not return any values.

    Examples
    --------
    >>> import pandas as pd
    >>> import xlwings as xw
    >>>
    >>> def dtypes_to_excel(df, sheet_name='Data Types'):
    ...     # Convert the dtypes Series to a DataFrame with string representations
    ...     dtypes_df = pd.DataFrame(df.dtypes.astype(str), columns=['Dtype'])
    ...     dtypes_df['Column'] = dtypes_df.index
    ...     dtypes_df = dtypes_df.reset_index(drop=True)[['Column', 'Dtype']]
    ...
    ...     # Use xlwings to export this DataFrame to Excel
    ...     app = xw.App(visible=True)
    ...     wb = app.books.add()
    ...     sheet = wb.sheets.add(sheet_name)
    ...
    ...     # Convert the DataFrame to a list of lists (including headers) for Excel
    ...     data_list = [dtypes_df.columns.tolist()] + dtypes_df.values.tolist()
    ...
    ...     # Write the data to Excel, starting from A1
    ...     sheet.range('A1').value = data_list
    ...
    ...     # Autofit columns for readability
    ...     sheet.autofit()
    ...
    >>> # Example usage
    >>> # Assuming 'df' is your DataFrame
    >>> dtypes_to_excel(df, 'DataFrame DataTypes')
    """
    # Convert the dtypes Series to a DataFrame with string representations
    dtypes_df = pd.DataFrame(df.dtypes.astype(str), columns=['Dtype'])
    dtypes_df['Column'] = dtypes_df.index
    dtypes_df = dtypes_df.reset_index(drop=True)[['Column', 'Dtype']]

    # Use xlwings to export this DataFrame to Excel
    app = xw.App(visible=True)
    wb = app.books.add()
    sheet = wb.sheets.add(sheet_name)

    # Convert the DataFrame to a list of lists (including headers) for Excel
    data_list = [dtypes_df.columns.tolist()] + dtypes_df.values.tolist()

    # Write the data to Excel, starting from A1
    sheet.range('A1').value = data_list

    # Autofit columns for readability
    sheet.autofit()
