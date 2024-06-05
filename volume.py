import math
from sphere import Sphere

def find_sphere_volume(sphere: Sphere) -> float:
    return (4 * math.pi * sphere.radius**3) / 3
