import xlwings as xw


def open_workbook(workbook_name: str) -> xw.main.Book:
    """
    Opens an Excel workbook as an app. If the workbook is already open, informs the user.
    If the file path is wrong, informs the user and offers to create a new workbook.

    Parameters:
    workbook_name (str): The name of the workbook to open, with extension.

    Returns:
    xw.main.Book: Workbook object for further operations or None if operation fails.

    Examples:
    # Open a workbook
    workbook = open_workbook("my_workbook.xlsx")

    # Do something with the workbook
    # ...

    # Close the workbook
    workbook.close()
    """
    try:
        app = xw.App(
            visible=True
        )  # Start a new Excel instance, make it visible
        # Check if the workbook is already open
        if workbook_name in (book.name for book in app.books):
            print(f"The workbook '{workbook_name}' is already open.")
            return None
        wb = app.books.open(workbook_name)  # Try to open the workbook
    except FileNotFoundError:
        # If the file doesn't exist, offer to create a new one
        create_new = input(
            f"The workbook '{workbook_name}' is missing. Do you want to create a new one? (yes/no): "
        )
        if create_new.lower() != "yes":
            print("Operation cancelled.")
            app.quit()
            return None
        wb = app.books.add()
        wb.save(workbook_name)
        print(f"New workbook '{workbook_name}' has been created and opened.")
    return wb
