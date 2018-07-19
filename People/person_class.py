import numpy as np
import pandas as pd


class person:
    """class for nodes in Neo4j database"""

    def __init__(self, id, relationships=[]):
        self.id = str(id)
        self.relationships = relationships

    """potentially write a relationship innerclass for more detail"""

    def add_relationship(self, other):
        self.relationships += other.id

    def __repr__(self):
        return "id = " + str(self.id) + "   Rel: " + str(self.relationships)

    def give_name(self, name: str):
        self.name = name
