from People import Generate
import pandas as pd
from timeit import default_timer
overall_population_size = 10000000
for i in range(25):
    start = default_timer()
    start_id = int(overall_population_size//25*i + 1)
    chunk = overall_population_size//25

    Pop = Generate.generate_population(chunk, start_id)

    Generate.generate_relationships_population(Pop, 3, 2, 10)

    array = Generate.build_relationship_array(Pop)
    if i == 0:
        df = pd.DataFrame(array, columns = ['person1_id', 'rel_id', 'person2_id'])
        df.to_csv('less_Relationships.csv', index=False)
    else:
        df = pd.DataFrame(array)
        df.to_csv('less_Relationships.csv', mode="a", index=False, header=False)
    #print(df)

    print("Time taken: ", default_timer() - start)