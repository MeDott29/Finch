from Finch.environmental import environments
from Finch.environmental.layers import standard_layers as layers
from Finch.environmental.layers import mutation_layers
from Finch.genetics import genepools
from textblob import TextBlob
import matplotlib.pyplot as plt
from Finch.functions import selection
rank = selection.RankBasedSelection(2, amount_to_select=10)
history = {}

def fit(individual):
    global history
    score = 0
    text = "".join(individual)
    words = text.split(" ")
    for i in words:
        try:
            points = history[i]
            score += points
        except:
            points = abs(TextBlob(i).polarity)
            history.update({i: points})
            score += points
    return score


gene_pool = genepools.StringPool("qwertyuiopasdfghjklzxcvbnm      ", length=50, fitness_function=fit)

environment = environments.Sequential(layers=[
    layers.Populate(gene_pool=gene_pool, population=4),
    mutation_layers.MutateAmount(amount_genes=2, gene_pool=gene_pool, selection_function=rank),
    layers.ParentSinglePointCrossover(5, 2, rank),
    layers.SortByFitness(),
    layers.CapPopulation(max_population=39),
])

environment.compile(verbose_every=500)
environment.evolve(10000)

print("".join(environment.individuals[0].genes))
print("VOCAB SIZE:")
print(len(history))
plt.plot(environment.history)
plt.show()