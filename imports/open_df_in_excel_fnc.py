import xlwings as xw
import pandas as pd  # Make sure to have pandas for DataFrame

def open_df_in_excel(
    dataframe: pd.DataFrame,
    sheet_name: str = "Sheet1",
    workbook: xw.Book = None,
) -> None:
    """
    Opens a given DataFrame in Excel at cell A1 of a specified sheet. Uses an existing workbook if provided,
    or opens a new workbook otherwise.

    Args:
        dataframe (pd.DataFrame): The DataFrame to open in Excel.
        sheet_name (str): The name of the sheet where the DataFrame should be opened. Defaults to 'Sheet1'.
        workbook (xw.Book, optional): The xlwings Book object (workbook) to use. If None, a new workbook is created.
    """
    # Check if a workbook is provided, else start Excel and add a new workbook
    if workbook is None:
        app = xw.App(visible=True)
        wb = app.books.add()  # Add a new workbook
    else:
        wb = workbook  # Use the provided workbook

    # Check if the specified sheet exists, and create it if not
    if sheet_name not in [s.name for s in wb.sheets]:
        wb.sheets.add(sheet_name)
    sheet = wb.sheets[sheet_name]

    # Clear the sheet (optional) and set the DataFrame to start at cell A1
    sheet.clear_contents()
    sheet.range("A1").options(index=False, header=True).value = dataframe

    # Excel is now open and visible to the user with the DataFrame displayed

# Example usage
"""
if __name__ == "__main__":
    # Create a simple example DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    # Open the DataFrame in Excel in a new workbook
    open_df_in_excel(df, sheet_name='MyData')

    # For using an existing workbook variable (assuming 'wb' is your xlwings workbook object)
    # open_df_in_excel(df, sheet_name='MyData', workbook=wb)
"""