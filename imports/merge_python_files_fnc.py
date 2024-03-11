import os

def merge_python_files(
    source_dir: str,
    output_file: str
    ) -> None:
    """
    Merges all Python files in the given source directory into a single file,
    writing the contents to the given output file.

    Args:
        source_dir (str): The directory containing the Python files to merge.
        output_file (str): The path of the file to write the merged contents to.

    Raises:
        FileExistsError: If the output file already exists.

    """
    if os.path.exists(output_file):
        raise FileExistsError(f"Output file {output_file} already exists. Please remove it or choose a different name.")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith('.py'):
                    # Construct the full file path
                    file_path = os.path.join(root, file)
                    print(f"Merging {file_path}...")

                    # Write a separator and the name of the current file
                    outfile.write(f"\n\n# {file}\n")

                    # Read the current file and write its contents to the output file
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())

    print(f"All files have been merged into {output_file}")

# Usage
# source_directory = '/path/to/python/files'
# output_filename = 'merged_files.py'
# merge_python_files(source_directory, output_filename)

merge_python_files('C:\\Users\\lunde\\repos\\_basic\\jupyter_starter\\imports', 'jupyter_helper_fnc.py')