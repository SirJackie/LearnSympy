import sympy as sp

sp.init_printing(use_unicode=True)

# # Define a Matrix
# mat = sp.Matrix([[1, -1], [3, 4], [0, 2]])
# sp.pprint(mat)

# # Matrix Multiplication
# M = sp.Matrix([[1, 2, 3], [3, 2, 1]])
# N = sp.Matrix([0, 1, 1])
# sp.pprint(M * N)

# Tip: One important thing to note about SymPy matrices is that,
# unlike every other object in SymPy, they are mutable.
# If you need an immutable version of Matrix, use ImmutableMatrix.

# # sp.shape() to check the shape of a Matrix
# # This can works in Sympy 1.9, but can't in Sympy 1.6.1
# M = sp.Matrix([[1, 2, 3], [-2, 0, 4]])
# print(sp.shape(M))

# # Access Individual rows and columns
# M = sp.Matrix([[1, 2, 3], [-2, 0, 4]])
# sp.pprint(M.row(0))
# sp.pprint(M.col(-1))

# Delete Rows and Column
M = sp.Matrix([[1, 2, 3], [-2, 0, 4]])
sp.pprint(M)
M.col_del(0)
M.row_del(1)
sp.pprint(M)
