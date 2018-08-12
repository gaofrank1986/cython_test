from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
npy_include_dir = numpy.get_include()

ext_modules = [Extension("mandel", ["pymandel.pyx"],
                         include_dirs = [npy_include_dir],
                         extra_objects=["mandel.o", "mandel_wrap.o"])]

setup(name = 'Mandelbrot fractals',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules)
