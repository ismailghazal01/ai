import numpy as np

class ScrapBooker:

    def crop(self, array, dim, position=(0, 0)):
        x, y = position
        h, w = dim
        try:
            return array[x:x+h, y:y+w]
        except:
            return None

    def thin(self, array, n, axis):
        try:
            if axis == 0:
                return np.delete(array, slice(n-1, None, n), axis=0)
            elif axis == 1:
                return np.delete(array, slice(n-1, None, n), axis=1)
        except:
            return None

    def juxtapose(self, array, n, axis):
        try:
            return np.concatenate([array]*n, axis=axis)
        except:
            return None

    def mosaic(self, array, dim):
        try:
            return np.tile(array, dim)
        except:
            return None