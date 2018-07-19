from People import Generate
from random import randint
import numpy as np
import multiprocessing as mp

from timeit import default_timer

if __name__ == "__main__":
    print('tits')
    def generate_relationships_population_parallel(pop, mean_number: int, rang: int, num_groups: int):
        # cuts population into chunks and generates relationships within each chunk
        groups = np.array_split(pop, num_groups)

        def generate_relationships_individual_parallel(individual):
            # This needs to inside in order to use the global variables
            individual.relationships = []
            population_size = len(group)
            i = 0
            n = randint(mean_number - rang, mean_number + rang)
            if n <= population_size:
                while i < n:
                    index = randint(0, population_size - 1)
                    another_individual = group[index]
                    # picks a person object from the group
                    if another_individual.id not in individual.relationships:
                        individual.relationships.append(another_individual.id)
                        i += 1
            else:
                pass

        for group in groups:
            mp.Pool().imap_unordered(generate_relationships_individual_parallel, group, len(group) // mp.cpu_count())

    # Calling previously defined functions and timing it
    start = default_timer()
    overall_population_size = 10000000

    Pop = Generate.generate_population(overall_population_size)

    generate_relationships_population_parallel(Pop, 3, 2, 10)
    print("time taken: ", default_timer() - start)
