from distutils.core import setup,Extension
#  from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy


ext_modules = [Extension("pyhello", ["pyhello.pyx"],
                         #  include_dirs = [npy_include_dir],
                         extra_objects=["hello.o"],
                         # need libgfortran for fortran write function
                         libraries = ['gfortran'],
                         library_dirs = ['/usr/local/lib'])
                         ]
setup(
        # need line below to carry out compiling, instead of using cythonize 
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules
        )
