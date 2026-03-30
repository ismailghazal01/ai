import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:

    def load(self, path):
        try:
            img = Image.open(path)
            arr = np.array(img) / 255.0
            print(f"Loading image of dimensions {arr.shape[0]} x {arr.shape[1]}")
            return arr
        except Exception as e:
            print(f"Exception: {type(e).__name__} -- strerror: {e}")
            return None

    def display(self, array):
        try:
            plt.imshow(array)
            plt.axis('off')
            plt.show()
        except:
            print("Error displaying image")