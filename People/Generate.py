import numpy as np
import multiprocessing as mp
import pandas as pd
from People import person_class
from random import randint


def generate_population(population_size, start_id=1):
    population = {}
    for i in range(start_id, start_id + population_size):
        a_person = person_class.person(i)
        population[a_person.id] = a_person
    return pd.Series(population)


def generate_relationships_individual(individual, step, population, number):
    # generates relationships for a person from a given population
    population_size = len(population)
    if True or step == 1:
        individual.relationships = []
        i = 0
        if number <= population_size:
            while i < number:
                index = randint(0, population_size - 1)
                another_individual = population[index]
                # picks a person object from the group
                if another_individual.id not in individual.relationships:
                    individual.relationships.append(another_individual.id)
                    i += 1
        else:
            pass

    # elif step == 2:
    # count = 0
    # while count < number:


def generate_relationships_population(pop, mean_number: int, rang: int, num_groups: int, ret=False):
    # cuts population into chunks and generates relationships within each chunk
    groups = np.array_split(pop, num_groups)

    for group in groups:

        for j in range(len(group)):
            n = randint(mean_number - rang, mean_number + rang)
            generate_relationships_individual(group[j], 1, group, n)
        # print(group, "dicks")
    if ret:
        return pop

def build_relationship_array(population):  # Will be edited to include more advanced relationships
    array = []
    for person in population:
        for relationship in person.relationships:
            array += [[person.id, 'placeholder', relationship]]
    return array





        # print(group, "dicks")"""