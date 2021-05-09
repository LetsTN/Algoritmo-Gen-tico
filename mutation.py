import random

class Mutation:
  def execute(self, chromosome):
    new_binary = ''

    for bit in chromosome.binary:
      bitM = bit
      mutation_rate = random.uniform(0, 1)

      if (mutation_rate <= 0.01):
        bitM = abs(int(bitM)-1)

      new_binary += str(bitM)

    chromosome.binary = new_binary
    chromosome.decoded = chromosome.decode()
    chromosome.fitness = chromosome.calc_fitness()
    return chromosome
