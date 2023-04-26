import os

from .build_for_py import build_docker_for_py
from .build_for_cpp import build_docker_for_cpp


def get_output(filename):
    """
    Generate output based on the given filename.

    Args:
        filename (str): The path of the file to generate output for.

    Returns:
        str: The generated output.

    Usage:
        To use this function, pass the filename of the file you want to generate output for as an argument.
        For example:
        get_output("example.py")
        This will generate output based on the contents of the "example.py" file and return it as a string.
    """
    extension = os.path.splitext(filename)[1]
    if extension == '.py':
        return build_docker_for_py(filename)
    elif extension == '.cpp' or extension == '.c':
        return build_docker_for_cpp(filename, extension)
