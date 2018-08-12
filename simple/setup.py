from distutils.core import setup,Extension
#  from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy
npy_include_dir = numpy.get_include()

ext_modules = [Extension("pytest", ["test.pyx"],
                         include_dirs = [npy_include_dir],
                         extra_objects=["test.o"],
                         # need libgfortran for fortran write function
                         libraries = ['gfortran'],
                         library_dirs = ['/usr/local/lib'])
                         ]
setup(
        # need line below to carry out compiling, instead of using cythonize 
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules
        )
