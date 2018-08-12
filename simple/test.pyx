from numpy cimport ndarray
from numpy import empty

cdef extern:
    void pythagoras(float *a, float *b, float *c);

def mesh_exp(float a, float b):
    #  cdef ndarray[float, mode="c"] mesh = empty(6, dtype="float")
    cdef float c
    pythagoras(&a, &b,&c)
    return c


