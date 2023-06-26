import numpy as np
cp = None
# Try importing CuPy
try:
    import cupy as cp

    # Check if GPU is available
    if cp.cuda.runtime.getDeviceCount() > 0:
        print("GPU detected. Using CuPy.")

        array_module = cp
        NPCP = cp
    else:
        print("GPU not detected. Using NumPy.")
        cp = np
        array_module = np

except ImportError:
    print("CuPy not found. Using NumPy.")
    array_module = np
set = False


def can_use_cupy(array):
    set = True
    # Check if the data type of the array is compatible with CuPy
    if np.issubdtype(array.dtype, np.number):
        return True
    # Check if the data type of the array can be safely cast to a CuPy-supported data type
    elif np.can_cast(array.dtype, cp.float64):
        return True
    # Otherwise, return False
    else:
        return False


NPCP = array_module


class Individual:
    def __init__(self, genes, fitness_function):
        global NPCP
        if set == False and cp and can_use_cupy(genes):
            NPCP = cp
        self.genes = NPCP.asarray(genes)  # Not sure if this will make it ineficiant if it already is the right type?
        # TODO
        self.fitness = 0
        self.fitness_function = fitness_function

    def fit(self):
        self.fitness = self.fitness_function(self.genes)

    def copy(self):  # this wont work with mutable fitness functions!!!
        copied_genes = NPCP.copy(self.genes)
        copied_fitness_function = self.fitness_function
        copied_individual = Individual(copied_genes, copied_fitness_function)
        copied_individual.fitness = self.fitness
        return copied_individual