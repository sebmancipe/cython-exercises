'''
Autor: Sebastian Mancipe
Clase: Fundamentos de Programación Paralela
Fecha: 22 de Noviembre del 2020
Universidad Sergio Arboleda
'''
'''
Este archivo le indica a Cython qué archivo fuente debe ser interpretado en C.
Se ejecuta con: python3 setup.py build_ext --inplace
'''


from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "heat_cy_openmp",
        ["heat_cy_openmp.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name='heat_cy_openmp',
    ext_modules=cythonize(ext_modules),
    include_dirs=[numpy.get_include()]
)