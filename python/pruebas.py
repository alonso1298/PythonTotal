import math

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return distancia

print(hay_colision(-1, 1, 3, 4))