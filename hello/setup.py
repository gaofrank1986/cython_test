from distutils.core import setup,Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

#  setup(
        #  ext_modules = cythonize("test.pyx"),
        #  include_dirs=[numpy.get_include()]
        #  )
#  ext_modules = [Extension("pyhello", ["pyhello.pyx"],
                         #  extra_objects=["hello.o"])]

ext_modules = [Extension("pyhello", ["pyhello.pyx"],
                         #  include_dirs = [npy_include_dir],
                         extra_objects=["hello.o"],
                         libraries = ['gfortran'],
                         library_dirs = ['/usr/local/lib'])
                         ]
setup(
        #  ext_modules = cythonize("test.pyx",include_path = [numpy.get_include()])
        #  ext_modules = cythonize(Extension("test",["test.pyx"], include_dirs=[numpy.get_include()]))
        #  ext_modules = cythonize("hello.pyx")
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules
        )
