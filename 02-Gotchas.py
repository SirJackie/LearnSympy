import sympy as sp

# # Symbol's Unchangeable Feature
# x = sp.symbols("x")
# expr = x + 1
# # x = 2  # This won't change expr
# print(expr)
# expr = expr.subs(x, 2)  # subs means substitute
# print(expr)

# Eq to create symbolic equalities
# x = sp.symbols("x")
# expr = sp.Eq(x + 1, 4)
# print(expr)

# # Check whether a == b
# x = sp.symbols("x")
# expr1 = (x + 1) ** 2
# expr2 = x**2 + 2*x + 1
# print(expr1, "---;---", expr2)
#
# # Method 1: Just check if a-b=0, need to use sp.simplify()
# expr3 = expr1 - expr2
# expr4 = sp.simplify(expr3)
# print(expr4)
#
# # Method 2: expr.equals(expr)
# print(expr3.equals(expr4))

# # Sympy v.s. Python's Types
# print(type(sp.Integer(1) + 1))
# print(type(1 + 1))

# Rational Division v.s. Float Division
print(1/2)
print(sp.Integer(1) / sp.Integer(2))
print(sp.Rational(1, 2))
