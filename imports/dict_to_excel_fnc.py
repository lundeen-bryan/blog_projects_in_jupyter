import xlwings as xw

def dict_to_excel(
    wb: xw.books.active,
    sheet_name: str,
    data_dict: dict[
        str, list[any]
    ]
    ) -> None:
    """
    Writes a dictionary to an Excel sheet in a workbook, starting from cell A1.

    Parameters:
    wb: xlwings Workbook object.
    sheet_name: String name of the Excel sheet to write data.
    data_dict: Dictionary with keys as categories and values as lists of variables.

    Returns:
    None

    Example:
    >>> import xlwings as xw
    >>> wb = xw.Book()  # Use an existing workbook or create a new one
    >>> sheet_name = 'VariableTypes'
    >>> data_dict = {
    ...     'categorical': ['model_year', 'origin', 'name'],
    ...     'numerical': ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']
    ... }
    >>> dict_to_excel(wb, sheet_name, data_dict)
    """
    # Ensure the sheet exists or create it
    if sheet_name in (sheet.name for sheet in wb.sheets):
        sheet = wb.sheets[sheet_name]
    else:
        sheet = wb.sheets.add(sheet_name)
    # Prepare data for Excel: convert dictionary to a list of lists
    # Including a header row (optional)
    data_for_excel = [["Category", "Variable"]]
    # Flatten the dictionary into a row for each value under each key
    for key, values in data_dict.items():
        for value in values:
            data_for_excel.append([key, value])
    # Write the prepared data to the sheet starting from A1
    sheet.range("A1").value = data_for_excel


# Usage example:

# Call the function to write the dictionary to the Excel sheet