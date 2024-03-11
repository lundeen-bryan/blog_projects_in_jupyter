def load_function(module_name, function_name):
    """
    Dynamically imports a specific function from a module, designed to work
    in a Jupyter notebook context or a standard Python script.

    Parameters
    ----------
    module_name : str
        The name of the module (without the .py extension).
    function_name : str
        The name of the function to import from the module.

    Returns
    -------
    function or None
        The imported function, or None if something went wrong.

    Examples
    --------
    Assume we have a Python module named 'math_operations.py' with a function named 'add':

    # math_operations.py
    def add(a, b):
        return a + b

    Here is how you can use `load_function` to dynamically load and use the 'add' function:

    >>> loaded_add_function = load_function("math_operations", "add")
    >>> if loaded_add_function:
    ...     result = loaded_add_function(2, 3)
    ...     print(f"Result: {result}")
    ...
    Result: 5
    """
    # Use the current working directory as the base for the 'imports' directory
    project_root = Path.cwd()  # This works if the notebook's working directory is the project root
    module_path = project_root / "imports" / f"{module_name}.py"

    spec = importlib.util.spec_from_file_location(module_name, str(module_path))
    if spec is None:
        print(f"Spec not found for module: {module_name}")
        return None

    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return getattr(module, function_name, None)
    except Exception as e:
        print(f"Error loading function {function_name} from module {module_name}: {e}")
        return None