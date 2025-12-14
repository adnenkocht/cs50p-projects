import math

def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)

side1 = "three"
side2 = 4.0
result = hypotenuse(side1, side2)

print(f"The hypotenuse is {result}")