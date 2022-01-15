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

# # Delete(Mutable) and Insert(Immutable) Rows and Column
# M = sp.Matrix([[1, 2, 3], [-2, 0, 4]])
# sp.pprint(M)
#
# # Delete
# M.col_del(0)
# sp.pprint(M)
# M.row_del(1)
# sp.pprint(M)
#
# # Insert
# M = M.row_insert(1, sp.Matrix([[0, 4]]))
# sp.pprint(M)
# M = M.col_insert(0, sp.Matrix([1, -2]))
# sp.pprint(M)

# # Transopse and Inversion
# M = sp.Matrix([[1, 2, 3], [-2, 0, 4], [3, 2, 1]])
# sp.pprint(M**-1)  # Inverse Matrix
# sp.pprint(M.T)  # Transpose Matrix

# # Matrix Calculation
# M = sp.Matrix([[1, 2], [3, 4]])
# N = sp.Matrix([[5, 6], [7, 8]])
#
# # Addition
# sp.pprint(M + N)
#
# # Multiplication
# sp.pprint(M * 2)
# sp.pprint(2 * M)
# sp.pprint(M * M)
# sp.pprint(M ** 2)  # The same as M * M

# # Identity Matrix
# sp.pprint(sp.eye(2))
# sp.pprint(sp.eye(3))
# sp.pprint(sp.eye(4))
# sp.pprint(sp.eye(5))
#
# # Zeros Matrix
# sp.pprint(sp.zeros(2))
# sp.pprint(sp.zeros(3))
# sp.pprint(sp.zeros(4))
# sp.pprint(sp.zeros(5))
# sp.pprint(sp.zeros(2, 3))
# sp.pprint(sp.zeros(3, 2))

# Ones Matrix
sp.pprint(sp.ones(2, 3))
sp.pprint(sp.ones(4))
