import pandas as pd
import xlwings as xw

def df_info_to_excel(df, sheet_name: str = 'DataFrame Info') -> None:
    """
    Writes a summary of a pandas DataFrame to an Excel sheet.

    Parameters:
    df: Pandas DataFrame to summarize.
    sheet_name: Name of the Excel sheet to write the summary to.

    Returns:
    None

    Example:
        import pandas as pd
        import xlwings as xw
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        df_info_to_excel(df, 'My Data')
    """
    # Create the DataFrame summary
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Non-Null Count': df.notnull().sum(),
        'Dtype': df.dtypes.astype(str),
    }).reset_index(drop=True)

    # Convert the DataFrame into a list of lists format for Excel
    info_data = [info_df.columns.tolist()] + info_df.values.tolist()

    # Start an instance of Excel and add a workbook
    app = xw.App(visible=True)
    wb = app.books.add()
    sheet_info = wb.sheets.add(sheet_name)

    # Write the structured info data to Excel, starting from A1
    sheet_info.range('A1').value = info_data

    # Correct the range for the table to match the info DataFrame's size
    last_row = len(info_df) + 1  # +1 to account for the header row
    table_range = f'A1:C{last_row}'

    # Create a table in Excel for the data range
    sheet_info.api.ListObjects.Add(SourceType=1, Source=sheet_info.range(table_range).api, XlListObjectHasHeaders=1)

    # Autofit the columns for readability
    sheet_info.autofit()
