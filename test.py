class Pokelib:
  def __init__(self):
      self.poke_list = []
      self.makePokeList()

  def makePokeList(self):
      self.poke_list.append(SPECIES_BULBASAUR)
      self.poke_list.append(SPECIES_IVYSAUR)



SPECIES_BULBASAUR = {
    "baseHP": 45,
    "baseAttack": 49,
    "baseDefense": 49,
    "baseSpeed": 45,
    "baseSpAttack": 65,
    "baseSpDefense": 65,

    #.safariZoneFleeRate : 0,
    #.bodyColor : BODY_COLOR_GREEN,
    #.noFlip : FALSE,
}

SPECIES_IVYSAUR = {
    "baseHP": 60,
    "baseAttack": 62,
    "baseDefense": 63,
    "baseSpeed": 60,
    "baseSpAttack": 80,
    "baseSpDefense": 80,

    #.safariZoneFleeRate : 0,
    #.bodyColor : BODY_COLOR_GREEN,
    #.noFlip : FALSE,
}
SPECIES_BULBASAUR['Power'] = SPECIES_BULBASAUR['baseHP'] + SPECIES_BULBASAUR['baseAttack']
