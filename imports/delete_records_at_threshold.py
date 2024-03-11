# coding: utf-8
import pandas as pd
import ipywidgets as widgets
from IPython.display import display

def delete_records_with_threshold(dataset):
    """
    This function is used to delete records from a dataset based on a given threshold.

    Parameters:
    dataset (pandas.DataFrame): The dataset to be processed.

    Returns:
    None

    """
    # Function to handle the deletion process
    def delete_records(b):
        threshold = threshold_slider.value / 100
        column_to_analyze = column_dropdown.value

        # Calculate missing data percentage for the selected column
        missing_percentage = dataset[column_to_analyze].isnull().mean()

        # Check against the threshold
        if missing_percentage <= threshold:
            # Delete records with missing values in the selected column
            initial_length = len(dataset)
            dataset.dropna(subset=[column_to_analyze], inplace=True)
            final_length = len(dataset)
            records_dropped = initial_length - final_length
            print(f"{records_dropped} records were dropped.")
        else:
            print(f"Threshold too low. Data loss would be substantial. No records were dropped.")

    # Dropdown for column selection
    column_dropdown = widgets.Dropdown(
        options=dataset.columns,
        description='Select Column:',
        disabled=False,
    )
    display(column_dropdown)

    # Slider for threshold selection
    threshold_slider = widgets.IntSlider(
        value=50,  # Default value
        min=0,     # Minimum value
        max=100,   # Maximum value
        step=1,    # Step size
        description='Threshold (%):',
        style={'description_width': 'initial'}
    )
    display(threshold_slider)

    # Button to confirm the deletion process
    delete_button = widgets.Button(description="Delete Records")
    display(delete_button)
    delete_button.on_click(delete_records)