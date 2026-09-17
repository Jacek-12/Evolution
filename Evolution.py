import random
import math

class Individuum:
  _fitness: float = 0

  def __init__(self, dna: list[float]):
    self._dna = dna
    # Sicherstellen, dass eine gültige DNA eingegeben wurde.

  def erstelle_dna(self):
    dna = []
    for i in range(4):
      dna.append(random.randint(0, 50))

    self._dna = dna

  def teste_fitness(self):
    durchschnitt = 0
    for i in self.dna:
      durchschnitt += i
    durchschnitt = durchschnitt / len(self.dna)

    fitness = 0
    for i in self.dna:
      fitness -= abs(durchschnitt - i)

    self._fitness = fitness

  def erstelle_mutation(slef):
    dna = []
    n = 0
    for i in slef.dna():
      u1 = random.random()
      u2 = random.random()
      z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

      dna.append(slef.dna()[n] + z)

      n += 1

    for i in dna:
      if i < 0:
        dna[dna.index(i)] = 0

      if i > 50:
        dna[dna.index(i)] = 50

    return Individuum(dna)

  def dna(self):
    return self._dna

  def fitness(self):
    return self._fitness

class Generation:
  _individuen: list[Individuum] = []

  def individuen(self):
    return self._individuen

  def append_individuum(self, individuum: Individuum):
    self._individuen.append(individuum)