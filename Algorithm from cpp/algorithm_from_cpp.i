%module algorithm_from_cpp

%include "std_vector.i"

%{
    #include <vector>
    #include <algorithm>
    #include "algorithm_from_cpp.hpp"
%}
namespace std {
    %template(IntVector) vector<int>;
    %template(vec_in_vec) vector<vector<int> >;


    %typemap(out) vector<vector<int> > (PyObject* _inner,PyObject* _outer) 
    %{
        // Allocate a PyList object of the requested size.
        _outer = PyList_New($1.size());
        // Populate the PyList.  PyLong_FromLong converts a C++ "long" to a
        // Python PyLong object.
        for(int x = 0; x < $1.size(); x++)
        {
            _inner = PyList_New($1[x].size());
            for(int y = 0; y < $1[x].size(); y++)
                PyList_SetItem(_inner,y,PyLong_FromLong($1[x][y]));
            PyList_SetItem(_outer,x,_inner);
        }
        $result = SWIG_Python_AppendOutput($result,_outer);
    %}

}


%include "algorithm_from_cpp.hpp"