import xlwings as xw
import pandas as pd

def load_data_into_excel(dataset: pd.DataFrame, file_path: str = 'mpg.xlsb', excel_visible: bool = True) -> None:
    """
    Loads dataset DataFrame into an Excel workbook with various sheets and tables.

    Parameters:
    - dataset: pandas DataFrame containing the dataset dataset.
    - file_path: String, the path and filename for saving the Excel workbook. Defaults to 'mpg.xlsb'.
    - excel_visible: Boolean, whether the Excel application should be visible. Defaults to True.
    """
    dataset_name = input("What is the name of the dataset? ").strip().lower()
    dataset_name_proper = dataset_name.upper()
    app = xw.App(visible=excel_visible)  # Start Excel application and make it visible or not based on the parameter
    wb = xw.Book()  # Create a new workbook

    # Create a head info sheet
    sheet_other = wb.sheets.add("Other")

    # Add header and data to the sheet as described
    sheet_other.range("A1").value = f"{dataset_name_proper} Dataset Shape"
    sheet_other.range("B1").value = "Rows"
    sheet_other.range("C1").value = "Columns"
    sheet_other.range("B2").value = dataset.shape
    sheet_other.range("A4").value = f"{dataset_name_proper} Dataset Columns"
    column_data = dataset.columns.to_list()
    sheet_other.range("B4").value = column_data
    sheet_other.range("A7").value = f"{dataset_name_proper} Dataset Data Types"
    dtypes_df = pd.DataFrame(dataset.dtypes.astype(str), columns=["DataType"]).reset_index()
    dtypes_df.columns = ["Column", "DataType"]
    sheet_other.range("B7").value = dtypes_df.columns.tolist()
    sheet_other.range("B8").value = dtypes_df.values.tolist()

    # Create and format tables
    table_data = [
        ("A1:C2", "shape_table"),
        ("A4:J5", "col_table"),
        ("A7:C16", "type_table"),
    ]
    for range_address, table_name in table_data:
        table = sheet_other.api.ListObjects.Add(
            SourceType=1,
            Source=sheet_other.api.Range(range_address),
            XlListObjectHasHeaders=1,
        )
        table.Name = table_name

    sheet_other.autofit()

    # Check and delete 'Sheet1' if it exists
    if 'Sheet1' in [s.name for s in wb.sheets]:
        wb.sheets['Sheet1'].delete()

    # Create a stats-describe() method sheet
    sheet_stats = wb.sheets.add("Stats")
    sheet_stats.range("A1").value = f"{dataset_name_proper} Dataset Statistics"
    sheet_stats.range("B1").value = dataset.describe()

    # Define table range for describe statistics and add a table
    table_data_stats = "A1:I9"
    table_stats = sheet_stats.api.ListObjects.Add(
        SourceType=1,
        Source=sheet_stats.api.Range(table_data_stats),
        XlListObjectHasHeaders=1
    )
    table_stats.Name = "stats_table"
    sheet_stats.autofit()

    # Manually create a DataFrame with the information aka info() method
    info_df = pd.DataFrame({
        'Column': dataset.columns,
        'Non-Null Count': dataset.notnull().sum(),
        'Dtype': dataset.dtypes.astype(str),
    }).reset_index(drop=True)

    # Add a sheet for info DataFrame and add a table
    sheet_info = wb.sheets.add('Info')
    info_data = [info_df.columns.tolist()] + info_df.values.tolist()
    sheet_info.range('A1').value = info_data
    table_info = sheet_info.api.ListObjects.Add(
        SourceType=1,
        Source=sheet_info.api.Range('A1:C' + str(len(info_df) + 1)),
        XlListObjectHasHeaders=1
    )
    table_info.Name = "dataset_info"
    sheet_info.autofit()

    wb.save(file_path)  # Save the workbook
    print(f"Workbook saved as '{file_path}'.")  # Inform the user
