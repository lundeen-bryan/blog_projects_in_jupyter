#!/bin/bash

# Function to print a prompt with text wrapping at 72 characters
print_prompt() {
  echo -e "$1" | fold -s -w 72
}

# Function to check if a Python package is installed
is_python_package_installed() {
    $python_exe -c "import $1" 2> /dev/null
    return $?
}

# Function to validate user input
validate_path() {
  local path="${1}"
  # Convert any backslashes in the path to forward slashes
  path="${path//\\//}"

  if [[ ! -e "$path" ]]; then
    print_prompt "Path does not exist. Exiting..."
    exit 1
  elif [[ ! -x "$path" ]]; then
    print_prompt "Path is not executable. Exiting..."
    exit 1
  fi
}

# Function to update requirements file
update_requirements() {
  local package_name="${1}"
  local version="${2}"

  if grep -q "^${package_name}==" requirements.txt; then
    local current_version=$(grep "^${package_name}==" requirements.txt | cut -d'=' -f3)
    if [ "$current_version" == "$version" ]; then
      print_prompt "The package '$package_name' is already at the latest version ($version)."
    else
      sed -i "/^${package_name}==/c\\${package_name}==${version}" requirements.txt
      print_prompt "The package '$package_name' has been updated to the latest version ($version) in requirements.txt."
    fi
  else
    echo "$package_name==$version" >> requirements.txt
    print_prompt "Package '$package_name' (version $version) has been added to requirements.txt."
  fi
}

# Function to write package name and latest version to requirements file
write_package_to_requirements() {
    package_name=$1
    version=$($python_exe -c "import requests; print(requests.get('https://pypi.org/pypi/$package_name/json').json()['info']['version'])" 2> /dev/null)
    if [ -z "$version" ]; then
        print_prompt "Package '$package_name' not found on PyPI. Please enter a valid package name."
        return 1
    fi
    update_requirements "$package_name" "$version"
    return 0
}

# Function to handle errors
handle_error() {
    print_prompt "An error occurred: $1"
    exit 1
}

# Function to clear the screen
clear_screen() {
    clear || printf "\033c"
}

# Prompt the user for the path to the Python executable
print_prompt "Enter the path to the Python executable: "
read python_exe
validate_path "$python_exe"

# Check if required Python packages are installed
if ! is_python_package_installed "requests"; then
    handle_error "'requests' Python package is not installed. Please install it before running this script."
fi

# Prompt for user confirmation
clear_screen
print_prompt "This script will write a package name and the latest version number to the requirements file. Do you want to continue? (yes/no): "
read choice

# Check user's choice
if [ "$choice" = "yes" ]; then
    while true; do
        # Read package name from user
        print_prompt "Enter the package name: "
        read package_name

        # Validate user input
        if [ -z "$package_name" ]; then
            handle_error "Package name cannot be empty."
        fi

        # Call function to write package to requirements file
        while true; do
            if ! write_package_to_requirements "$package_name"; then
                print_prompt "Package '$package_name' not found. Please enter the package name again: "
                read package_name
            else
                break
            fi
        done

        # Prompt to add another package
        print_prompt "Do you want to add another package? (yes/no): "
        read choice

        # Check user's choice
        if [ "$choice" = "no" ]; then
            break
        elif [ "$choice" != "yes" ]; then
            handle_error "Invalid choice. Please enter 'yes' or 'no'."
        fi

        clear_screen
    done

    print_prompt "Script execution completed."
else
    print_prompt "Script execution canceled."
fi

