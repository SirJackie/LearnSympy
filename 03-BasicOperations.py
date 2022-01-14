import sympy as sp

# # Substitution
# # Tip: expr.subs() returns a new expression. SymPy objects are immutable.
# # That means that subs does not modify it in-place.
# # The creating process of expr2 does not modify expr1
# x = sp.symbols("x")
# expr1 = sp.cos(x) + sp.Integer(1)
# expr2 = expr1.subs(x, 0)
# print(expr1)
# print(expr2)

# # Multiple Substitution
# x, y, z = sp.symbols("x y z")
# expr1 = x**3 + 4*x*y - z
# expr2 = expr1.subs([(x, 2), (y, 4), (z, 0)])
# print(expr1)
# print(expr2)

# # SYMPY-fy AKA sp.sympify()
# strExpr = "(x + 1) ** 2"
# expr = sp.sympify(strExpr)
# print(expr)

# sp.evalf() to evaluate the expressions into float number
x = sp.symbols("x")
expr = (x + 1) ** 2
print(expr.subs(x, 1).evalf())
print(sp.pi.evalf())
print(sp.pi.evalf(100))
