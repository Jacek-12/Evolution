import random

class Individuum:
  fitness: float = 0

  def __init__(self, dna: list[float]):
    self._dna = dna

  @property
  def dna(self):
    return self._dna

class Generation:
  _individuen: list[Individuum] = []

  def individuen(self):
    return self._individuen

  def append_individuum(self, individuum: Individuum):
    self._individuen.append(individuum)

def erstelle_dna():
  dna = []
  for i in range(4):
    dna.append(random.randint(0, 50))
  return dna

def teste_fitness(individuum: Individuum):
  durchschnitt = 0
  for i in individuum.dna:
    durchschnitt += i
  durchschnitt = durchschnitt / len(individuum.dna)
  # Nähe der einzelnen DNAteile zum Durchschnitt messen.