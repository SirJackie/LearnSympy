import sympy as sp

sp.init_printing(use_unicode=True)

A = sp.MatrixSymbol('A', 2, 2)
B = sp.MatrixSymbol('B', 2, 2)
C = A * B

sp.pprint(A)
sp.pprint(B)
sp.pprint(C)

nC = C.subs(
        {
            A: sp.Matrix([[0, 1], [1, 0]]),
            B: sp.Matrix([[2, 3], [4, 5]])
        }
    )

sp.pprint(nC)
