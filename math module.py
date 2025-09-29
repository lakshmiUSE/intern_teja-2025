Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#math module
#case1
import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.factorial(5)
120
factorial(5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    factorial(5)
NameError: name 'factorial' is not defined
NameError: name 'factorial' is not defined
SyntaxError: invalid syntax





math.floor(9.8)
9
from math import factorial
factorial(5)
120
floor(9.8)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    floor(9.8)
NameError: name 'floor' is not defined. Did you mean: 'float'?
>>> from math import factorial,floor
>>> factorial(5)
120
>>> floor(9.8)
9
>>> from math import *
>>> factorial(5)
120
>>> sin(90)
0.8939966636005579
>>> sqrt(4)
2.0
>>> import math as m
>>> m.floor(2.0)
2
>>> from math import factorial as f
>>> f(5)
120
