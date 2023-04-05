import os

from .build_for_py import build_docker_for_py
from .build_for_cpp import build_docker_for_cpp


def get_output(filename):
    extension = os.path.splitext(filename)[1]
    if extension == '.py':
        return build_docker_for_py(filename)
    elif extension == '.cpp' or extension == '.c':
        return build_docker_for_cpp(filename, extension)
