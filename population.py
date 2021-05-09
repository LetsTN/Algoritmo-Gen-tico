import random

from chromosome import Chromosome

class Population:
  def __init__(self, population):
    self.population = population

  def start_population(self):
    population_list = []

    for i in range(self.population):
      binary = self.build_binary()
      chromosome = Chromosome(binary)
      chromosome.decoded = chromosome.decode()
      chromosome.fitness = chromosome.calc_fitness()
      population_list.append(chromosome)

    return population_list

  def build_binary(self):
    length = 16
    binary = ''

    for i in range(length):
      bit = random.randint(0, 1)
      binary += str(bit)

    return binary
