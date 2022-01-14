import sympy as sp

x = sp.symbols("x")
expr = x + 1
print(expr)
expr = expr.subs(x, 2)  # subs means substitute
print(expr)
