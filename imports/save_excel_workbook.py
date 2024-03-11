import xlwings as xw

def save_workbook(filename=None):
    """
    Saves the active xlwings workbook. If a filename is provided, it saves the workbook with that name.
    If no filename is provided and the workbook already has a name, it saves using the existing name.
    If the workbook has no name and no filename is provided, an error will be raised.

    Parameters:
    - filename: Optional. The full path and filename where the workbook should be saved.
                If not provided, the workbook's current name and path are used.
    """
    # Get the active workbook
    wb = xw.books.active

    # If no filename is provided, check if the workbook already has a name
    if filename is None:
        if wb.fullname:
            # Save with the current name and path
            wb.save()
            print(f"Workbook saved using existing name and path: {wb.fullname}")
        else:
            # Raise an error if the workbook has no name and no filename is provided
            raise ValueError("A filename must be provided for workbooks that have not been previously saved.")
    else:
        # Save with the provided filename
        wb.save(filename)
        print(f"Workbook saved as {filename}")
