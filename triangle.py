import math
from random import randint


class Triangle:
    """A class used to represent a right triangle
    
    Attributes
    ----------
    a: int
        length of side a

    b: int
        length of side b
    """

    def __init__(self, a, b):
        "Create triangle from a and b sides."
        self.a = a
        self.b = b
        self.c = self.get_hypotenuse()

    def __repr__(self):
        return f"Triangle a={self.a} b={self.b}"

    def get_hypotenuse(self):
        """Get hypotenuse (length of 3rd side)."""
        return math.sqrt(self.a ** 2 + self.b ** 2)

    @classmethod
    def random(cls):
        """Class method which returns Triangle with random sides"""
        return cls(randint(1,20), randint(1,20))

    def get_area(self):
        "Get area of triangle"
        return (self.a * self.b) / 2

    def describe(self):
        return f"I am a triangle with sides: {self.a} & {self.b}"
    
# def rand_triangle():
#     return Triangle(3,4)