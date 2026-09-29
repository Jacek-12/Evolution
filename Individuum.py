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

    self.dna = dna

  @property
  def dna(self):
    return self.dna