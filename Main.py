from Individuum import Individuum
import random

class Main:
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

    for Individuum in aktuelle_generation:
      Individuum.fitness = self.teste_fitness(Individuum.dna)

    schlechteste_fitness = aktuelle_generation[0].fitness
    beste_fitness = aktuelle_generation[0].fitness

    for Individuum in aktuelle_generation:
      if Individuum.fitness < schlechteste_fitness:
        schlechteste_fitness = Individuum.fitness

      if Individuum.fitness > beste_fitness:
        beste_fitness = Individuum.fitness

    if schlechteste_fitness == beste_fitness:
      ueberlebende_individuen = random.choice(aktuelle_generation, k=(self.groesse_generationen / 2))
    else:
      gewichte = []
      for Individuum in aktuelle_generation:
        gewichte.append(Individuum.fitness - schlechteste_fitness)

      ueberlebende_individuen = random.choice(aktuelle_generation, gewichte, k=(self.groesse_generationen / 2))

    self.generationen.append(ueberlebende_individuen)
    # Neue Individuen anhängen.