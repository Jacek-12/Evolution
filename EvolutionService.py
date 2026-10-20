from Individuum import Individuum
import random
import numpy as np

class EvolutionService:
  def __init__(self, erstelle_dna: function, erstelle_mutation: function, teste_fitness: function, groesse_generationen: int):
    if groesse_generationen <= 0:
      raise ValueError("Die größer der Generationen ist <= 0.")

    if groesse_generationen % 2 == 1:
      raise ValueError("Die größer der Generation ist ungerade.")

    self.erstelle_mutation = erstelle_mutation
    self.teste_fitness = teste_fitness
    self.groesse_generationen = groesse_generationen

    self.generationen: list[list[Individuum]] = [[]]
    for i in range(self.groesse_generationen):
      self.generationen[0].append(Individuum(erstelle_dna()))

  def erstelle_naechste_generation(self):
    aktuelle_generation = self.generationen[len(self.generationen) - 1]

    for individuum in aktuelle_generation:
      individuum.fitness = self.teste_fitness(individuum.dna)

    schlechteste_fitness = aktuelle_generation[0].fitness
    beste_fitness = aktuelle_generation[0].fitness

    for individuum in aktuelle_generation:
      if individuum.fitness < schlechteste_fitness:
        schlechteste_fitness = individuum.fitness

      if individuum.fitness > beste_fitness:
        beste_fitness = individuum.fitness

    if schlechteste_fitness == beste_fitness:
      ueberlebende_individuen = random.sample(
        aktuelle_generation,
        k=self.groesse_generationen // 2
      )
    else:
      gewichte = []
      for individuum in aktuelle_generation:
        gewichte.append(individuum.fitness - schlechteste_fitness)

      ueberlebende_individuen: list[Individuum] = list(
        np.random.choice(
          aktuelle_generation,
          size=self.groesse_generationen // 2,
          replace=False,
          p=np.array(gewichte) / sum(gewichte)
        )
      )

    neu_generation = ueberlebende_individuen.copy()
    for individuum in ueberlebende_individuen:
      neu_generation.append(Individuum(self.erstelle_mutation(individuum.dna), individuum.id))

    self.generationen.append(neu_generation)

  def gib_ueberlebende_individuen_zwischen(self, generation_a: int, generation_b: int):
    if not (generation_a < len(self.generationen) and generation_a >= 0):
      raise ValueError("generation_a ist nicht in generationen enthalten.")

    if not (generation_b < len(self.generationen) and generation_b >= 0):
      raise ValueError("generation_b ist nicht in generationen enthalten.")

    return [
      individuum
      for individuum in self.generationen[generation_a]
      if individuum in self.generationen[generation_b]
    ]