# Finch

Finch is a genetic algorithm library for Python focused on flexibility and ease of use.
## Docs
These are very much a work in progress but should be helpful!
- https://finch-1.gitbook.io/finch/
## Key Features

- Layer-based environments for composable evolution
- Multiple built-in environments like Sequential and Adversarial  
- Genepools for genes like integers, floats, strings, and binary
- Flexible selection and mutation functions
- Built-in fitness functions for common tasks 
- GPU acceleration with CuPy for larger populations

## Environments
"""
The key features of Finch include layer-based environments for composable evolution, multiple built-in environments like Sequential and Adversarial, genepools for genes like integers, floats, strings, and binary, flexible selection and mutation functions, built-in fitness functions for common tasks, and GPU acceleration with CuPy for larger populations. These features make Finch a versatile and powerful tool for creating and manipulating genetic algorithms. For example, the layer-based environments allow users to compose their own evolutionary algorithms, while the multiple built-in environments provide a variety of contexts in which these algorithms can evolve. The genepools provide a range of gene types that can be used in the algorithms, and the flexible selection and mutation functions allow users to control how these genes are selected and mutated. The built-in fitness functions provide common metrics for evaluating the fitness of individuals in the population, and the GPU acceleration with CuPy allows for efficient computation with larger populations.
"""

- **Sequential**: Evolve through a predefined sequence of layers
- **Adversarial**: Compare multiple environments and evolve the best performer
- **Chronological**: Switch environments at specified generations
- **Adaptive**: Automatically switch environments based on performance

## Layers

- **Populate**: Initialize a population from a genepool
- **MutateAmount**: Mutate a number of genes in selected individuals
- **Parent**: Recombine selected parents into new individuals
- **SortByFitness**: Sort the population by fitness
- **CapPopulation**: Cull the population down to a max size
  
## Genepools  
"""
The layers in Finch include Populate, MutateAmount, Parent, SortByFitness, and CapPopulation. The Populate layer allows for the initialization of a population from a genepool. The MutateAmount layer allows for the mutation of a number of genes in selected individuals. The Parent layer allows for the recombination of selected parents into new individuals. The SortByFitness layer allows for the sorting of the population by fitness. The CapPopulation layer allows for the culling of the population down to a max size. These layers provide a variety of operations that can be performed on a population, and they can be used in combination to create complex evolutionary algorithms. For example, a user might start with a Populate layer to create an initial population, then use a MutateAmount layer to introduce variation, a Parent layer to create new individuals, a SortByFitness layer to select the best performers, and finally a CapPopulation layer to maintain a manageable population size.
"""

- **IntPool**: Generate genes as integer values
- **FloatPool**: Generate genes as float values
- **BinaryPool**: Generate binary integer genes 
- **StringPool**: Generate string genes
"""
Finch is a genetic algorithm library for Python. It is designed with a focus on flexibility and ease of use. The library provides a variety of features that allow users to create and manipulate genetic algorithms. These features include layer-based environments for composable evolution, multiple built-in environments like Sequential and Adversarial, genepools for genes like integers, floats, strings, and binary, flexible selection and mutation functions, built-in fitness functions for common tasks, and GPU acceleration with CuPy for larger populations. The documentation for Finch is currently a work in progress, but it should be helpful for users who want to learn more about the library and how to use it.
"""
- **OutlinesPool**: Generate guided text using the Outlines library

## AI Features (very early)

Finch includes tools for evolving AI models and prompts:

### Layers

- **LlmPromptMutation**: Mutate prompts with a language model  
- **PromptParenting**: Generate new prompts by recombining with a language model

### Genepools

- **KerasPool**: Evolve the weights of a Keras model
- **PyTorchPool**: Evolve the weights of a PyTorch model
"""
The environments in Finch include Sequential, Adversarial, Chronological, and Adaptive. The Sequential environment allows for evolution through a predefined sequence of layers. The Adversarial environment allows for the comparison of multiple environments and the evolution of the best performer. The Chronological environment allows for the switching of environments at specified generations. The Adaptive environment allows for the automatic switching of environments based on performance. These environments provide a variety of contexts in which genetic algorithms can evolve, and they can be used in combination to create complex evolutionary scenarios. For example, a user might start with a Sequential environment to establish a basic population, then switch to an Adversarial environment to select the best performers, and finally switch to an Adaptive environment to fine-tune the evolution based on performance.
"""
- **TensorFlowPool**: Evolve the weights of a TensorFlow model
- **PromptPool**: Generate prompt genes with a language model

Finch makes it easy to customize and combine predefined building blocks into a tailored evolutionary algorithm. The adversarial and adaptive environments provide automated optimization not found in other libraries. With CuPy support and fitness analysis tools, Finch enables scaling up experiments and tracking progress.
# Detailed Documentation

Detailed documentation for Finch provides comprehensive insights into its design principles, architecture, functionalities, and usage examples. The detailed documentation includes specifics on the genepools, layers, selection and mutation functions, and guidance on how to optimize and evolve AI models using the library. It is an essential resource for practitioners looking to harness the power of genetic algorithms for scalable and flexible solutions.

For more detailed documentation, please refer to the `DOCS.md` file.
"""
The genepools in Finch include IntPool, FloatPool, BinaryPool, StringPool, and OutlinesPool. The IntPool generates genes as integer values. The FloatPool generates genes as float values. The BinaryPool generates binary integer genes. The StringPool generates string genes. The OutlinesPool generates guided text using the Outlines library. These genepools provide a variety of gene types that can be used in genetic algorithms, and they can be used in combination to create complex gene structures. For example, a user might use an IntPool to generate integer genes for a numerical optimization problem, a StringPool to generate string genes for a text generation problem, and an OutlinesPool to generate guided text for a structured text generation problem.
"""
