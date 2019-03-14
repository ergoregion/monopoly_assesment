from .sites import MonopolySite
from .state import MonopolyState
import numpy as np


class MonopolyModel(object):
    def __init__(self):
        self.sites = [s for s in MonopolySite]
        self._prepare_states()
        self.dof = len(self.states)

        self.state_vector = np.zeros(self.dof, dtype=np.float)

        self._prepare_transmission_matrix()

    def _prepare_states(self):
        # board position only
        self.states = [MonopolyState(s) for s in self.sites]

    def _prepare_transmission_matrix(self):
        # stay where you are
        m = np.zeros((self.dof, self.dof), dtype=np.float)
        for i in range(40):
            m[i,(i+2)%40]  = 1/36.0
            m[i,(i+3)%40]  = 2/36.0
            m[i,(i+4)%40]  = 3/36.0
            m[i,(i+5)%40]  = 4/36.0
            m[i,(i+6)%40]  = 5/36.0
            m[i,(i+7)%40]  = 6/36.0
            m[i,(i+8)%40]  = 7/36.0
            m[i,(i+9)%40]  = 6/36.0
            m[i,(i+10)%40]  = 5/36.0
            m[i,(i+11)%40]  = 4/36.0
            m[i,(i+12)%40]  = 3/36.0
            m[i,(i+13)%40]  = 2/36.0
            m[i,(i+14)%40]  = 1/36.0

        self.transmission_matrix = m
