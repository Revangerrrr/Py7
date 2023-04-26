import numpy as np
from PIL import Image


def bw_convert(path):
    image = np.asarray(Image.open(path), dtype='uint8')
    x, y, z = image.shape
    bw = np.array([[[0.2989, 0.587, 0.114]]])
    image2 = np.round(np.sum(image * bw, axis=2)).astype(np.uint8).reshape(x, y)
    Image.fromarray(image2).save('123123.jpg')


bw_convert('maxresdefault.jpg')
