from Neo4j import Generate
from random import randint
import numpy as np
import multiprocessing as mp
import pandas as pd
from timeit import default_timer
from Neo4j.person_class import person

""""MULTIPROCESSING CAN ONLY CALL TOP LEVEL FUNCTIONS"""
if __name__ == "__main__":
    print('tits')

    overall_population_size = 10000 -7
    number = 5  # 1st division
    sub_number = mp.cpu_count() # second division
    print("cpu core count is " + str(sub_number) +
          "\ngroup size is approximately " + str(overall_population_size//(number * sub_number)))
    for i in range(number):
        start = default_timer()
        pool = mp.Pool()
        pop = pd.Series([])


        def append_pop(sub_pop):
            """append function outside of loop for stupid multiprocessing reasons"""
            global pop
            pop = pop.append(sub_pop)


        for j in range(sub_number):
            start_id = int(
                overall_population_size // number // sub_number * j  # iterate j, double floored division
                + overall_population_size // (number) * i + 1  # iterate i
            )
            print(start_id)
            # added robustness
            if j == sub_number - 1 and i == number - 1:
                print("end chunk")
                chunk = overall_population_size // (number * sub_number) + (overall_population_size // number) % sub_number+ overall_population_size % number
                print(chunk)
            elif j == sub_number - 1:
                chunk = overall_population_size // (number * sub_number) + (overall_population_size // number) % sub_number
                print("inter chunk", chunk)
            else:
                chunk = overall_population_size // (number * sub_number)
            sub_pop = Generate.generate_population(chunk, start_id)
            # rewrite pop with relationships
            sub_pop = pool.apply_async(Generate.generate_relationships_population,
                                       (sub_pop, 1, 1, 10, True,), callback=append_pop)
            # pop = pop.append(sub_pop)

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
