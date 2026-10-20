import random
import math
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

def teste_fitness(dna: list[float]):
  durchschnitt = 0
  for i in dna:
    durchschnitt += i
  durchschnitt = durchschnitt / len(dna)

  for i in dna:
    fitness = abs(durchschnitt - i) * -1

  return fitness

groesse_generationen = 100

evolution_server = EvolutionService(erstelle_dna, erstelle_mutation, teste_fitness, groesse_generationen)

runing = True
while runing:
  evolution_server.erstelle_naechste_generation()

  ueberlebende_individuen = evolution_server.gib_ueberlebende_individuen_zwischen(len(evolution_server.generationen) - 2, len(evolution_server.generationen) - 1)

  letzte_generation_sortiert = evolution_server.generationen[len(evolution_server.generationen) - 2].sort(key=lambda individuum: individuum.fitness, reverse=True)

  for individuum in evolution_server.generationen[len(evolution_server.generationen) - 2]:
    if individuum in ueberlebende_individuen:
      for individuum_letzte_generation in evolution_server.generationen[len(evolution_server.generationen) - 1]:
        if individuum_letzte_generation.eltern_id == individuum.id:
          kind_individuum = individuum_letzte_generation
          break

      print([round(x, 2) for x in individuum.dna], individuum.id, "->", [round(x, 2) for x in individuum_letzte_generation.dna], individuum_letzte_generation.id)
    else:
      print([round(x, 2) for x in individuum.dna], individuum.id, "-> X")

  if input("next? ") == "n":
    runing = False