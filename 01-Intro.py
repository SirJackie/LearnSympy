import sympy as sp

# x = sp.sqrt(8)
# print(x)

# x, y = sp.symbols("x y")
# expr = x + 2 * y
# print(expr)
# print(expr + 1)
# print(expr - x)
# print(expr - y)
# print(x * expr)  # No further simplification

# x, y = sp.symbols("x y")
# expr = x * (x + 2 * y)
# expandedExpr = sp.expand(expr)
# factoredExpr = sp.factor(expandedExpr)
# print(expr, "; ", expandedExpr, "; ", factoredExpr)

x = sp.symbols("x")
print(sp.solve(x**2-2, x))
