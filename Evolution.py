import random
import math

class Individuum:
  fitness: float = 0

  def __init__(self, dna: list[float]):
    if not isinstance(dna, list):
      raise TypeError("die übergebene DNA ist keine liste.")

    if len(dna) > 4:
      raise ValueError("Die DNA enthält mehr als 4 Elemente.")

    for i in dna:
      if not isinstance(i, float):
        raise TypeError("Die DNA enthält mindestens eine Element das keine float ist.")

      if i < 0 or i > 50:
        raise ValueError("Die DNA enthält mindestens ein Element das größer als 50 oder kleiner als 0 ist.")

    self._dna = dna

  def erstelle_dna(self):
    dna = []
    for i in range(4):
      dna.append(random.randint(0, 49) + random.random())

    self._dna = dna

  def erstelle_mutation(slef):
    dna = []
    n = 0
    for i in slef.dna():
      u1 = random.random()
      if u1 == 0:
        u1 = 1

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

class Generation:
  _individuen: list[Individuum] = []

  def individuen(self):
    return self._individuen

  def append_individuum(self, individuum: Individuum):
    self._individuen.append(individuum)

def teste_fitness(dna: list[float]):
  durchschnitt = 0
  for i in dna:
    durchschnitt += i
  durchschnitt = durchschnitt / len(dna)

  for i in dna:
    fitness = abs(durchschnitt - i) * -1

  return fitness

generationen = [Generation()]
for i in range(100):
  generationen[0].append_individuum(Individuum([0.0, 0.0, 0.0, 0.0]))
  generationen[0].individuen()[i].erstelle_dna()

running = True
while running:
  gewichte: list[float] = []
  for i in generationen[len(generationen) - 1].individuen():
    i.fitness = teste_fitness(i.dna())
    gewichte.append(i.fitness)

  kleinstes_gewicht = 1
  for i in gewichte:
    if i > kleinstes_gewicht:
      kleinstes_gewicht = i

  x = 0
  for i in gewichte:
    gewichte[x] = i - kleinstes_gewicht

  ueberlebende_individuen = random.choice(generationen[len(generationen) - 1].individuen(), gewichte, k=(math.floor(generationen[len(generationen) - 1].individuen() / 2)))
# Hier weiter machen.