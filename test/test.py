from heat_main_cy_openmp import main as heat_main_cy_openmp
from heat_main_cy_1 import main as heat_main_cy_1
from heat_main_cy_2 import main as heat_main_cy_2
from heat_main_py import main as heat_main_py

from timeit import repeat

niterations = 10

# Pure Python
time_python = repeat("heat_main_py()", number=niterations, repeat=1, globals=locals())
time_python = min(time_python) / niterations

# Cython with no optimization
time_cython = repeat("heat_main_cy_1()", number=niterations, repeat=1, globals=locals())
time_cython = min(time_cython) / niterations

# Cython with optimization
time_cython_opt = repeat("heat_main_cy_2()", number=niterations, repeat=1, globals=locals())
time_cython_opt = min(time_cython_opt) / niterations

# Cython with openmp
time_cython_openmp = repeat("heat_main_cy_openmp()", number=niterations, repeat=1, globals=locals())
time_cython_openmp = min(time_cython_openmp) / niterations

print("Pure Python:                                {:5.3f} s".format(time_python))
print("Cython:                                     {:5.3f} s".format(time_cython))
print("Speedup:                                    {:5.1f}".format(time_python / time_cython) - 1)
print("Cython with optimization:                   {:5.3f} s".format(time_cython_opt))
print("Speedup over Cython:                        {:5.1f}".format(time_cython / time_cython_opt) - 1)
print("Cython with optimization and OpenMP:        {:5.3f} s".format(time_cython_openmp))
print("Speedup over Cython with optimization:      {:5.1f}".format(time_cython_opt / time_cython_openmp) - 1)
