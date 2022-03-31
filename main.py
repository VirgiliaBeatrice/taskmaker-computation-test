from random import Random
from tkinter import Image
import numpy as np
import matplotlib.pyplot as plt
import skia
from PIL import Image
# from numpy.typing import  { np.ndarray }

class RectVoronoiRegion:

    def __init__(self) -> None:
        pass

    @staticmethod
    def create_rect_region(a: np.ndarray, b: np.ndarray, factor=50):
        dir: np.ndarray = b - a
        std_dir: np.ndarray = dir / np.linalg.norm(dir)
        perp: np.ndarray = np.dot(RectVoronoiRegion.get_rotation_mat(90), std_dir)

        aP = a + perp * factor
        bP = b + perp * factor

        return (a, b, bP.ravel(), aP.ravel())

    @staticmethod
    def get_rotation_mat(angle: float):
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)

        rotation_mat = np.array(((c, -s), (s, c)))

        return rotation_mat


if __name__ == '__main__':
    width, height = 200, 200
    array = np.zeros((height, width, 4), dtype=np.uint8)

    r1 = Random().randrange(0, 200)
    r2 = Random().randrange(0, 200)

    a = np.array((r1, r2))
    b = np.array((60, 120))

    (a, b, bP, aP) = RectVoronoiRegion.create_rect_region(a, b)

    with skia.Surface(array) as canvas:
        canvas.clear(skia.ColorWHITE)
        canvas.drawCircle(a[0], a[1], 5.0, skia.Paint(Color=skia.Color(204, 0, 0, 255)))
        canvas.drawCircle(b[0], b[1], 5.0, skia.Paint(Color=skia.Color(0, 0, 255, 255)))
        canvas.drawCircle(bP[0], bP[1], 5.0, skia.Paint(Color=skia.Color(0, 0, 255, 124)))
        canvas.drawCircle(aP[0], aP[1], 5.0, skia.Paint(Color=skia.Color(204, 0, 0, 124)))

    im = Image.fromarray(array)
    im.show()
    # plt.imshow(array)
    # plt.show()
