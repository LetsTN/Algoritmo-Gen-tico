import math
import random

from chromosome import Chromosome

class Crossover:
  def execute(self, chromosome_A, chromosome_B):
    crossover_rate = random.uniform(0, 1)

    if (crossover_rate <= 0.6):
      return self.crossover_chromosomes(chromosome_A, chromosome_B)
    else:
      return chromosome_A, chromosome_B

  def crossover_chromosomes(self, chromosome_A, chromosome_B):
    chromosome_lenght = len(chromosome_A.binary)
    split = random.randint(1, chromosome_lenght-1)

    part_1A = chromosome_A.binary[:split]
    par_2A = chromosome_A.binary[split:]
    part_1B = chromosome_B.binary[:split]
    part_2B = chromosome_B.binary[split:]

    son_1_binary = part_1A + part_2B
    son_1 = Chromosome(son_1_binary)
    son_1.decoded = son_1.decode()
    son_1.fitness = son_1.calc_fitness()

    son_2_binary = part_1B + par_2A
    son_2 = Chromosome(son_2_binary)
    son_2.decoded = son_2.decode()
    son_2.fitness = son_2.calc_fitness()

    return son_1, son_2
