import numpy as np

class ColorFilter:

    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        new = np.zeros_like(array)
        new[:, :, 2] = array[:, :, 2]
        return new

    def to_green(self, array):
        new = array.copy()
        new[:, :, [0,2]] = 0
        return new

    def to_red(self, array):
        new = array.copy()
        new[:, :, [1,2]] = 0
        return new

    def to_celluloid(self, array):
        new = array.copy()
        levels = np.linspace(0, 1, 5)
        for i in range(len(levels)-1):
            mask = (new >= levels[i]) & (new < levels[i+1])
            new[mask] = levels[i]
        return new

    def to_grayscale(self, array, filter, **kwargs):
        if filter in ['m', 'mean']:
            gray = array.mean(axis=2)
        elif filter in ['w', 'weight']:
            r = kwargs.get('r_weight')
            g = kwargs.get('g_weight')
            b = kwargs.get('b_weight')
            gray = array[:,:,0]*r + array[:,:,1]*g + array[:,:,2]*b
        else:
            return None
        return np.stack((gray,)*3, axis=-1)