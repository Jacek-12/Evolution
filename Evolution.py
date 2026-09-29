import random
import math

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
      u1 = 1

    u2 = random.random()

    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    neue_dna.append(dna[n] + z)

    n += 1

  for i in neue_dna:
    if i < 0:
      neue_dna[neue_dna.index(i)] = 0

    if i > 50:
      neue_dna[neue_dna.index(i)] = 50

  return neue_dna

def teste_fitness(dna: list[float]):
  durchschnitt = 0
  for i in dna:
    durchschnitt += i
  durchschnitt = durchschnitt / len(dna)

  for i in dna:
    fitness = abs(durchschnitt - i) * -1

  return fitness