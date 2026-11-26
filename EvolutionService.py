from Individuum import Individuum
import numpy as np
from typing import Callable

class EvolutionService:
  def __init__(self, erstelle_dna: Callable[[], list[float]], erstelle_mutation: Callable[[list[float]], list[float]], teste_fitness: Callable[[list[Individuum]], None], groesse_generationen: int):
    if groesse_generationen <= 0:
      raise ValueError("Die Größer der Generationen ist <= 0.")

    if groesse_generationen % 2 == 1:
      raise ValueError("Die Größer der Generation ist ungerade.")

    self._erstelle_mutation = erstelle_mutation
    self._teste_fitness = teste_fitness
    self._groesse_generationen = groesse_generationen
    self.aktuelle_fitness = None

    self.generationen: list[list[Individuum]] = [[]]
    for i in range(self._groesse_generationen):
      self.generationen[0].append(Individuum(erstelle_dna()))

  @property
  def groesse_generationen(self):
    return self._groesse_generationen

  def teste_fitness(self):
    self._teste_fitness(self.generationen[-1])
    aktuelle_fitness: list[float] = []
    for individuum in self.generationen[-1]:
      aktuelle_fitness.append(individuum.fitness)

    anzahl_fitness_groesser_null = 0
    for i in aktuelle_fitness:
      if not isinstance(i, float):
        raise TypeError("Ein Element der Fitness ist keine Fließkommerzahl.")
      if i < 0:
        raise ValueError("Ein Element der Fitness ist kleiner als 0.")
      if i > 0:
        anzahl_fitness_groesser_null += 1
    if anzahl_fitness_groesser_null < len(aktuelle_fitness) // 2:
      raise ValueError("Mindestens die Hälfte der Individuen müssen eine Fitnes > 0 haben.")

    if sum(aktuelle_fitness) == 0:
      raise ValueError("Die Summe aus den Fitness darf nicht 0 sein.")

    self.aktuelle_fitness = aktuelle_fitness

  def erstelle_naechste_generation(self):
    if self.aktuelle_fitness == None:
      self.teste_fitness()

    ueberlebende_individuen: list[Individuum] = list(
      np.random.choice(
        self.generationen[-1],
        size=self._groesse_generationen // 2,
        replace=False,
        p=np.array(self.aktuelle_fitness) / sum(self.aktuelle_fitness)
      )
    )

    neu_generation = ueberlebende_individuen.copy()
    for individuum in ueberlebende_individuen:
      neu_generation.append(Individuum(self._erstelle_mutation(individuum.dna), individuum.id))

    self.generationen.append(neu_generation)

    self.aktuelle_fitness = None

  def gib_ueberlebende_individuen_zwischen(self, generation_a: int, generation_b: int):
    if not (generation_a < len(self.generationen) and generation_a >= (-1 * len(self.generationen))):
      raise ValueError("generation_a ist nicht in generationen enthalten.")

    if not (generation_b < len(self.generationen) and generation_b >= (-1 * len(self.generationen))):
      raise ValueError("generation_b ist nicht in generationen enthalten.")

    return [
      individuum
      for individuum in self.generationen[generation_a]
      if individuum in self.generationen[generation_b]
    ]