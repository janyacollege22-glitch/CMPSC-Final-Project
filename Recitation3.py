class Complex:
    """ Complex number of the form a + bi where a and b are 
    real numbers, and i is an indeterminate satisfiying  i**2 = -1
    """

    def __init__(self, r, i):
        self._real = r
        self._imag = i

    def conjugate(self):
        """ Return a complex object that represents the complex conjugate"""
        return Complex(self._real, -self._imag)
    
    def __mul__(self, other):
        """ Multiply two complex numbers """
        if isinstance(other, Complex):
            real_part = self._real * other._real - self._imag * other._imag
            imag_part = self._real * other._imag + self._imag * other._real
            ans = Complex(real_part, imag_part)
        else:
            real_part = self._real * other
            imag_part = self._imag * other
            ans = Complex(real_part, imag_part)
        return ans
    def __rmul__(self, other):
        """ Multiply two complex numbers """
        return self*other
    
    def __str__(self):
        """Display Complex number"""
        if self._imag >= 0:
            return f"{self._real}+{self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    __repr__=__str__

class Real(Complex):
    """ Real number of the form a + 0i where a is a real number"""
    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self, other):
        """ Multiply two real numbers """
        if isinstance(other, Real):
            real_part = self._real * other._real
            ans = Real(real_part)
        elif isinstance(other, (int, float)):
            real_part = self._real * other
            ans = Real(real_part)
        elif isinstance(other, Complex):
            real_part = self._real * other._real
            imag_part = self._real * other._imag
            ans = Complex(real_part, imag_part)
        return ans
    def __eq__(self, other):
        """ Check if two real numbers are equal """
        if isinstance(other, Real):
            return self._real == other._real
        elif isinstance(other, (int, float)):
            return self._real == other
        elif isinstance(other, Complex):
            return self._real == other._real and other._imag == 0

        else:
            return False    
    def __int__(self):
        """ Return the integer representation of the real number """
        return int(self._real)
    
    def __float__(self):
        """ Return the float representation of the real number """  
        return self._real
    