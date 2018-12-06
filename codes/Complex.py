import numpy as np

class Complex (object):
    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self,other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self,other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __div__(self, other):
        r = float( other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real + self.real * other.imag) / r , (self.imag * other.real -self.real * other.imag) / r)
    def __abs__(self):
        return np.sqrt(self.real ** 2 + self.imag ** 2)
    def __neg__(self):
        return Complex(-self.real, -self.imag)
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    def print(self):
        print(self.real,str(self.imag)+"j")
    def phase(self):
        return np.arctan2(self.imag, self.real)* 180 / np.pi

x = Complex(1,1)
y = Complex (2,2)
z = x+y
z.print()
z = x - y
z.print()
z = -z
z.print()
z = x*y
z.print()
y = Complex (4,10)
x = Complex (10,1)
z = x*y
z.print()
print(z.phase())
print(abs(z))

