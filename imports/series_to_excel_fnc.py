import xlwings as xw
import pandas as pd


def series_to_excel(
    series: pd.Series,
    sheet_name: str = "Series Data",
    include_index: bool = True,
) -> None:
    """
    Export a pandas Series to an Excel worksheet.

    Args:
        series (pd.Series): The pandas Series to export.
        sheet_name (str, optional): The name of the worksheet to create.
            Defaults to "Series Data".
        include_index (bool, optional): Whether to include the index as a
            column in the Excel worksheet. Defaults to True.

    Returns:
        None

    Example usage:
        # Use the series_to_excel function
        series_to_excel(series, "My Series Data")

        # Open the Excel file and check the results
        app = xw.App(visible=True)
        wb = app.books.open("My Excel File.xlsx")
        sheet = wb.sheets["My Series Data"]

        print(sheet.range("A1").value)
    """
    app = xw.App(visible=True)
    wb = app.books.add()
    sheet = wb.sheets.add(sheet_name)

    if include_index:
        # Convert the Series to a DataFrame to include the index
        data_to_export = series.reset_index()
        # Convert DataFrame to a list of lists and include headers
        data_list = [
            data_to_export.columns.tolist()
        ] + data_to_export.values.tolist()
    else:
        # Handle the Series directly without the index
        data_list = [[series.name]] + series.values.reshape(-1, 1).tolist()

    # Write the data to Excel, starting from A1
    sheet.range("A1").value = data_list

    # Autofit columns for better readability
    sheet.autofit()
