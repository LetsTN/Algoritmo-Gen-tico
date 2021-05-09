import random
import copy

from chromosome import Chromosome
from population import Population
from crossover import Crossover
from mutation import Mutation

class Genetic_Algorithm:
  def __init__(self, generation):
    self.population = 10
    self.generation = generation

  def get_best_from_population(self, population_list):
    selected = []

    for i in range(len(population_list)):
      random_1 = random.randint(0, len(population_list)-1)
      chromosome_1 = copy.deepcopy(population_list[random_1])

      random_2 = random.randint(0, len(population_list)-1)
      chromosome_2 = copy.deepcopy(population_list[random_2])

      if (chromosome_1.fitness < chromosome_2.fitness):
        selected.append(chromosome_1)
      else:
        selected.append(chromosome_2)

    return selected

  def get_new_population(self, selected):
    new_population = []

    for i in range(0, len(selected), 2):
      chromosome_A = selected[i]
      chromosome_B = selected[i+1]
      
      son_1, son_2 = Crossover().execute(chromosome_A, chromosome_B)

      new_population.append(Mutation().execute(son_1))
      new_population.append(Mutation().execute(son_2))
    
    return new_population

  def execute(self):
    best = []

    population_list = Population(self.population).start_population()

    for i in range(self.generation):
      selected = self.get_best_from_population(population_list)

      new_population = self.get_new_population(selected)

      new_population = sorted(new_population, key=Chromosome.get_fitness)

      worst = new_population[-1]

      population_list = sorted(population_list, key=Chromosome.get_fitness)
      best_parent = population_list[0]

      if (worst.fitness > best_parent.fitness):
        for i in range(len(new_population)):
          if new_population[i].fitness == worst.fitness:
            del new_population[i]
            break

        new_population.append(best_parent)

      new_population = sorted(new_population, key=Chromosome.get_fitness)
      current_best = new_population[0]

      best.append(current_best)

    return best

