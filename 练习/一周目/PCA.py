import numpy as np

class CPCA:
    def __init__(self,X,K):
        self.X = X
        self.K = K
        self.centrX = []
        self.C = []
        self.U = []
        self.Z = []

        self.centrX = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()  # Z=XU求得
