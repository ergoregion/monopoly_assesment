from monopoly.model.sites import MonopolySite
from enum import Enum

class StateVariation(Enum):
    FINISHED = 0
    ROLLED_DOUBLE = 1,
    ROLLED_DOUBLE_2 = 2,
    ROLLED_DOUBLE_3 = 3,
    CARD_UNTAKEN = 4,
    STILL_TO_MOVE = 5,

class JailStateVariation(Enum):
    NONE =0,
    JUST_ARRIVED = 1,
    TURN_2 = 2,
    TURN_3 =3,



class MonopolyState(object):
    def __init__(self, site: 'MonopolySite', variation: 'StateVariation', jail_state = JailStateVariation.NONE):
        self.site: 'MonopolySite' = site
        self.variation: 'StateVariation' = variation
        self.jail_state: 'JailStateVariation' = jail_state

    def __repr__(self):
        if self.jail_state:
            return self.site.name + self.jail_state.name
        else:
            return self.site.name + self.variation.name
