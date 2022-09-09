from z3 import *

n = int(input("n (in bits):"))
print("BinarySub: a = d - b")
b = input("b (in n bits):")
d = input("d (in n bits):")

A = [Bool('A_%i' % (i+1)) for i in range(n)]
B = [Bool('B_%i' % (i+1)) for i in range(n)]
C = [Bool('C_%i' % (i+1)) for i in range(n)]
D = [Bool('D_%i' % (i+1)) for i in range(n)]
C0 = Bool('C_0')

b_c = [
    If(b[i]=='1', B[i], Not(B[i]))
    for i in range(n)
]
d_c = [
    If(d[i]=='1', D[i], Not(D[i]))
    for i in range(n)
]
sum_c = [
    And(
        Implies(
            D[i],
            And(
                Implies(
                    A[i],
                    And(
                        Implies(B[i], C[i]),
                        Implies(C[i], B[i])
                    )
                ),
                Implies(
                    And(
                        Implies(B[i], C[i]),
                        Implies(C[i], B[i])
                    ),
                    A[i]
                )
            )
        ),
        Implies(
            And(
                Implies(
                    A[i],
                    And(
                        Implies(B[i], C[i]),
                        Implies(C[i], B[i])
                    )
                ),
                Implies(
                    And(
                        Implies(B[i], C[i]),
                        Implies(C[i], B[i])
                    ),
                    A[i]
                )
            ),
            D[i]
        )
    )
    for i in range(n)
]
carry_c = [
    And(
        Implies(
            C[i-1],
            Or(
                And(A[i], B[i]),
                And(A[i], C[i]),
                And(B[i], C[i])
            )
        ),
        Implies(
            Or(
                And(A[i], B[i]),
                And(A[i], C[i]),
                And(B[i], C[i])
            ),
            C[i-1]
        )
    )
    for i in range(1, n)
]
leftmost_carry = [And(
    Implies(
        C0,
        Or(
            And(A[0], B[0]),
            And(A[0], C[0]),
            And(B[0], C[0])
        )
    ),
    Implies(
        Or(
            And(A[0], B[0]),
            And(A[0], C[0]),
            And(B[0], C[0])
        ),
        C0
    )
)]
leftmost_carry_c = [Not(C0)]
rightmost_carry_c = [Not(C[n-1])]

solve(b_c + d_c + sum_c + carry_c + leftmost_carry + leftmost_carry_c + rightmost_carry_c)