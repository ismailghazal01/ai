import numpy as np

class NumpyCreator:

    def from_list(self, lst):
        try:
            return np.array(lst)
        except:
            return None

    def from_tuple(self, tpl):
        try:
            return np.array(tpl)
        except:
            return None

    def from_iterable(self, itr):
        try:
            return np.array(list(itr))
        except:
            return None

    def from_shape(self, shape, value=0):
        try:
            return np.full(shape, value)
        except:
            return None

    def random(self, shape):
        try:
            return np.random.rand(*shape)
        except:
            return None

    def identity(self, n):
        try:
            return np.eye(n)
        except:
            return None