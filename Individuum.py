import uuid

class Individuum:
  fitness: float = 0.0

  def __init__(self, dna: list[float], eltern_id: str | None = None):
    if not isinstance(dna, list):
      raise TypeError("Die übergebene DNA ist keine liste.")

    if len(dna) != 4:
      raise ValueError("Die DNA muss genau 4 Elemente enthalten.")

    for i in dna:
      if not isinstance(i, float):
        raise TypeError("Die DNA enthält mindestens eine Element das keine float ist.")

      if i < 0 or i > 50:
        raise ValueError("Die DNA enthält mindestens ein Element das größer als 50 oder kleiner als 0 ist.")

    self._dna = dna
    self._eltern_id = eltern_id

    self._id = uuid.uuid4()

  @property
  def dna(self):
    return self._dna

  @property
  def id(self):
    return self._id

  @property
  def eltern_id(self):
    return self._eltern_id