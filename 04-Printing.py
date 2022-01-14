import sympy as sp
from sympy.printing.mathml import print_mathml
from sympy.printing.dot import dotprint

x = sp.symbols("x")
expr = sp.Integral(sp.sqrt(1/x), x)

# Direct Printing (Python Syntax Form)
print(expr)
print(str(expr))

# Unicode Printing
sp.init_printing(use_latex=False)
sp.pprint(expr)
print(sp.pretty(expr))

# ASCII Printing
sp.init_printing(use_latex=False, use_unicode=False)
sp.pprint(expr)
print(sp.pretty(expr))

# Latex, MathML and Dot Printing
print(sp.latex(expr))
print(print_mathml(expr))
print(dotprint(expr))
