import random
import math
from Individuum import Individuum
from EvolutionService import EvolutionService

def erstelle_dna():
  dna = []
  for i in range(4):
    dna.append(random.randint(0, 49) + random.random())

  return dna

def erstelle_mutation(dna: list[float]):
  neue_dna = []
  n = 0
  for i in dna:
    u1 = random.random()
    if u1 == 0:
      u1 = 1.0

    u2 = random.random()

    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    neue_dna.append(dna[n] + z)

    n += 1

  for i in neue_dna:
    if i < 0:
      neue_dna[neue_dna.index(i)] = 0.0

    if i > 50:
      neue_dna[neue_dna.index(i)] = 50.0

  return neue_dna

def teste_fitness(generation: list[Individuum]):
  fitness_generation = []
  schlechteste_fitness = 0
  for individuum in generation:
    durchschnitt = sum(individuum.dna) / len(individuum.dna)
    fitness = 0.0

    for i in individuum.dna:
      fitness -= abs(durchschnitt - i)

    if fitness < schlechteste_fitness:
      schlechteste_fitness = fitness

    fitness_generation.append(fitness)

  laenge_fitness_generation = len(fitness_generation)
  for i in range(laenge_fitness_generation):
    fitness_generation[i] -= schlechteste_fitness - 1

  x = 0
  for individuum in generation:
    individuum.fitness = fitness_generation[x]
    x += 1

groesse_generationen = 100

evolution_server = EvolutionService(erstelle_dna, erstelle_mutation, teste_fitness, groesse_generationen)

runing = True
while runing:
  for i in range(100):
    evolution_server.erstelle_naechste_generation()

    ueberlebende_individuen = evolution_server.gib_ueberlebende_individuen_zwischen(-2, -1)

    letzte_generation_sortiert = sorted(
      evolution_server.generationen[-2],
      key=lambda individuum: individuum.fitness,
      reverse=True
    )

    for x in range(2):
      individuum: Individuum = letzte_generation_sortiert[0 - x]
      if individuum in ueberlebende_individuen:
        for individuum_letzte_generation in evolution_server.generationen[-1]:
          if individuum_letzte_generation.eltern_id == individuum.id:
            kind_individuum = individuum_letzte_generation
            break

        print([round(x, 2) for x in individuum.dna], individuum.fitness, "->", [round(x, 2) for x in individuum_letzte_generation.dna])
      else:
        print([round(x, 2) for x in individuum.dna], individuum.fitness, "-> X")

  if input("stop? ") == "stop":
    runing = False