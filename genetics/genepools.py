from Finch.genetics.population import *


class Pool:
    def __init__(self):
        pass


class DefaultPool(Pool):
    def __init__(self, valid_genes: np.ndarray, length: int, fitness_function):
        super().__init__()
        self.valid_genes = valid_genes
        self.length = length
        self.fitness_function = fitness_function

    def generate(self):
        return Individual(NPCP.random.choice(self.valid_genes, size=self.length), self.fitness_function)

    def generate_genes(self, num_genes):
        return NPCP.random.choice(self.valid_genes, size=num_genes)


class FloatPool(Pool):
    def __init__(self, minimum_float, maximum_float, length: int, fitness_function, default=None):
        super().__init__()
        self.minimum_gene = minimum_float
        self.maximum_gene = maximum_float
        self.length = length
        self.fitness_function = fitness_function
        self.default = default

    def generate(self):
        if self.default is not None:
            genes = NPCP.full(self.length, self.default)
        else:
            genes = NPCP.random.uniform(self.minimum_gene, self.maximum_gene, size=self.length)
        return Individual(genes, self.fitness_function)

    def generate_genes(self, num_genes):
        return NPCP.random.uniform(self.minimum_gene, self.maximum_gene, size=num_genes)


class IntPool(Pool):
    def __init__(self, minimum_int, maximum_int, length: int, fitness_function):
        super().__init__()
        self.minimum_gene = minimum_int
        self.maximum_gene = maximum_int
        self.length = length
        self.fitness_function = fitness_function

    def generate(self):
        genes = NPCP.random.randint(self.minimum_gene, self.maximum_gene + 1, size=self.length)
        return Individual(genes, self.fitness_function)

    def generate_genes(self, num_genes):
        return NPCP.random.randint(self.minimum_gene, self.maximum_gene + 1, size=num_genes)


class BinaryPool(Pool):
    def __init__(self, length: int, fitness_function):
        super().__init__()
        self.length = length
        self.fitness_function = fitness_function

    def generate(self):
        genes = NPCP.random.randint(0, 2, size=self.length)
        return Individual(genes, self.fitness_function)

    def generate_genes(self, num_genes):
        return NPCP.random.randint(0, 2, size=num_genes)


class StringPool(Pool):
    def __init__(self, valid_characters: str, length: int, fitness_function):
        super().__init__()
        self.valid_characters = valid_characters
        self.length = length
        self.fitness_function = fitness_function

    def generate(self):
        genes = np.random.choice(list(self.valid_characters), size=self.length)
        return Individual(genes, self.fitness_function)

    def generate_genes(self, num_genes):
        genes = np.random.choice(list(self.valid_characters), size=(num_genes, self.length))
        return ["".join(gene) for gene in genes]


class PermutationPool(Pool):
    def __init__(self, valid_genes: np.ndarray, length: int, fitness_function):
        super().__init__()
        self.valid_genes = valid_genes
        self.length = length
        self.fitness_function = fitness_function

    def generate(self):
        genes = NPCP.random.permutation(self.valid_genes)[:self.length]
        return Individual(genes, self.fitness_function)

    def generate_genes(self, num_genes):
        genes = NPCP.random.permutation(self.valid_genes)[:num_genes * self.length]
        return NPCP.split(genes, num_genes)


