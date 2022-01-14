import sympy as sp

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
