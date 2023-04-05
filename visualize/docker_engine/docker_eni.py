import os
import build_for_py
import build_for_cpp


def get_output(filename):
    extension = os.path.splitext(filename)[1]
    if extension == '.py':
        return build_for_py.build_docker_for_py(filename)
    elif extension == '.cpp' or extension == '.c':
        return build_for_cpp.build_docker_for_cpp(filename, extension)
