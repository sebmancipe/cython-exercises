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


from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("heat.pyx"), include_dirs=[numpy.get_include()])