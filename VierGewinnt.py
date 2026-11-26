from enum import Enum

class Spieler(Enum):
  SPIELER_A = "Spieler_A"
  SPIELER_B = "Spieler_B"

class VierGewinnt:
  spielbrett = [
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None], 
    [None, None, None, None, None, None]
  ]

  spieler = Spieler.SPIELER_A

  def ziehe(self, spalte: int):
    # Prüfen, ob das Spiel nicht schon vorbei ist.

    if spalte < 0 or spalte > 6:
      raise ValueError("Der Parameter spalte muss zwischen 0 und 6 sein.")

    if None not in self.spielbrett[spalte]:
      raise ValueError(f"Die Spalte {spalte} ist voll.")

    self.spielbrett[spalte][self.spielbrett[spalte].index(None)] = self.spieler

    if self.spieler == Spieler.SPIELER_A:
      self.spieler = Spieler.SPIELER_B
    else:
      self.spieler = Spieler.SPIELER_A

  # Spielzustand Prüfen Gewinner, Unentschieden ...