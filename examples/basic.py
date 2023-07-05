from Finch.environmental import environments
from Finch.environmental import layers
from Finch.genetics import genepools
from Finch.functions import selection


def fit(individual):
    return "".join(individual).count("a")


gene_pool = genepools.StringPool("qwertyuiopasdfghjklzxcvbnm", length=20, fitness_function=fit)

environment = environments.Sequential(layers=[
    layers.Populate(gene_pool=gene_pool, population=4),
    layers.MutateAmount(amount_individuals=10, amount_genes=3, gene_pool=gene_pool),
    layers.Parent(num_children=4, num_families=4),
    layers.SortByFitness(),
    layers.CapPopulation(max_population=20),
])

environment.evolve(100, verbose_every=1)

print(environment.individuals[0].genes)