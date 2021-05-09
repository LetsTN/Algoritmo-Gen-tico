import math

class Chromosome:
  def __init__(self, binary):
    self.binary = binary
    self.fitness = None
    self.decoded = None

  def get_fitness(self):
    return self.fitness

  def decode(self):
    bits = len(self.binary)
    decimal = int(self.binary, 2)
    return -20 + ((20+20) * (decimal / (2**bits-1)))

  def calc_fitness(self):
    return (math.cos(self.decoded) * self.decoded) + 2