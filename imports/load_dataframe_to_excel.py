import xlwings as xw
import pandas as pd  # Make sure to have pandas for DataFrame

def open_df_in_excel(dataframe, sheet_name="Sheet1"):
    """
    Opens a given DataFrame in Excel at cell A1 of a specified sheet.

    Args:
    - dataframe (pd.DataFrame): The DataFrame to open in Excel.
    - sheet_name (str): The name of the sheet where the DataFrame should be opened. Defaults to 'Sheet1'.
    """
    # Start an instance of Excel
    app = xw.App(visible=True)
    wb = app.books.add()  # Add a new workbook

    # Check if the specified sheet exists, and create it if not
    if sheet_name not in [s.name for s in wb.sheets]:
        wb.sheets.add(sheet_name)
    sheet = wb.sheets[sheet_name]

    # Clear the sheet (optional) and set the DataFrame to start at cell A1
    sheet.clear_contents()
    sheet.range('A1').options(index=False, header=True).value = dataframe

    # Excel is now open and visible to the user with the DataFrame displayed

# Example usage
# if __name__ == "__main__":
#     # Create a simple example DataFrame
#     df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

#     # Open the DataFrame in Excel
#     open_df_in_excel(df, sheet_name='MyData')
