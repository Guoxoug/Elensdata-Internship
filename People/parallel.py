from People import Generate
from random import randint
import numpy as np
import multiprocessing as mp
import pandas as pd
from timeit import default_timer
from People.person_class import person

""""MULTIPROCESSING CAN ONLY CALL TOP LEVEL FUNCTIONS"""
if __name__ == "__main__":
    print('tits')

    """def generate_relationships_population_parallel(pop, mean_number: int, rang: int, num_groups: int):
        # cuts population into chunks and generates relationships within each chunk
        groups = np.array_split(pop, num_groups)
        new_pop = []

        def generate_relationships_individual_parallel(individual, mean_number, rang, group):
            # This needs to inside in order to use the global variables which is a dodgy trick to remember
            new_individual = person(individual.id)
            new_individual.relationships = []
            population_size = len(group)
            i = 0
            n = randint(mean_number - rang, mean_number + rang)
            new_individual.relationships.append("1")
            if n <= population_size:
                while i < n:
                    index = randint(0, population_size - 1)
                    another_individual = group[index]
                    # picks a person object from the group
                    if another_individual.id not in new_individual.relationships:
                        new_individual.relationships.append(another_individual.id)
                        i += 1
            else:
                pass
            # needs to return something otherwise multiprocessing won't work
            return new_individual

        def generate_relationships_inside(pop, mean_number: int, rang: int, num_groups: int):
            population_chunk = []
            for individual in pop:
                new_individual = person(individual.id)
                new_individual.relationships = []
                population_size = len(pop)
                i = 0
                n = randint(mean_number - rang, mean_number + rang)
                new_individual.relationships.append("1")
                if n <= population_size:
                    while i < n:
                        index = randint(0, population_size - 1)
                        another_individual = pop[index]
                        # picks a person object from the group
                        if another_individual.id not in new_individual.relationships:
                            new_individual.relationships.append(another_individual.id)
                            i += 1
                population_chunk.append(new_individual)
            return population_chunk

        with mp.Pool() as pool:
            for group in groups:
                group.tolist()

                new_pop += pool.apply_async(generate_relationships_inside, (group, mean_number,rang,
                                                                                num_groups,)).get()

            pool.close()
            pool.join()
        return new_pop

    # Calling previously defined functions and timing it
    start = default_timer()
    overall_population_size = 1000000

    Pop = Generate.generate_population(overall_population_size)

    Pop = generate_relationships_population_parallel(Pop, 3, 2, 10)

    array = Generate.build_relationship_array(Pop)

    df = pd.DataFrame(array, columns=['person1_id', 'rel_id', 'person2_id'])
    df.to_csv('less_Relationships1.csv', index=False)

    print("time taken: ", default_timer() - start)
    print(Pop[0])"""
    # DOESN@T IMPROVE SPEED CONSIDER USING A NESTED FOR LOOP
    overall_population_size = 1000000
    number = 3
    sub_number = mp.cpu_count()

    for i in range(number):
        start = default_timer()
        pool = mp.Pool()
        pop = pd.Series([])
        def append_pop(sub_pop):
            global pop
            pop = pop.append(sub_pop)
        for j in range(sub_number):
            start_id = int(
                overall_population_size // (number * sub_number) * j
                 + overall_population_size // (number) * i + 1)
            print(start_id)
            chunk = overall_population_size // (number * sub_number)
            sub_pop = Generate.generate_population(chunk, start_id)
            # rewrite pop with relationships
            sub_pop = pool.apply_async(Generate.generate_relationships_population, (sub_pop, 3, 2, 10, True,), callback=append_pop)
            #pop = pop.append(sub_pop)


        pool.close()
        pool.join()
        array = Generate.build_relationship_array(pop)
        if i == 0:
            df = pd.DataFrame(array, columns=['person1_id', 'rel_id', 'person2_id'])
            df.to_csv('less_Relationships.csv', index=False)
        else:
            df = pd.DataFrame(array)
            df.to_csv('less_Relationships.csv', mode="a", index=False, header=False)
        # print(df)

        print("Process: " + str(i) + "\nTime taken: ", default_timer() - start)
