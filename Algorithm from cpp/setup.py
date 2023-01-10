from setuptools import setup, Extension

algorithm_module = Extension("_algorithm_from_cpp", sources = ['algorithm_from_cpp_wrap.cxx', 'algorithm_from_cpp.cpp'], language = 'c++', extra_compile_args = ['/std:c++17'],)  #其中的名字，与自己编写的文件对应就好，“_test”即模块名称，必须要有下划线

setup(
    name = 'algorithm_from_cpp',
    version = '0.1',
    author = 'SWIG Docs',
    description = 'Simple swig pht from docs',
    ext_modules = [algorithm_module],py_modules = ['algorithm_from_cpp'],) #除了与模块名有关的内容，其他的信息可以自己修改