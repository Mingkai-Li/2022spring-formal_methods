from z3 import *
import time

n = int(input("n:"))
Q = [[Bool("Q_%s_%s" % (i+1, j+1)) for j in range(n)] for i in range(n)]
row_exist = [Or([Q[i][j] for j in range(n)]) for i in range(n)]
row_distinct = [
    If(j==k, True, Or(Not(Q[i][j]), Not(Q[i][k])))
    for k in range(n) for j in range(k)
    for i in range(n)
]
col_exist = [Or([Q[i][j] for i in range(n)]) for j in range(n)]
col_distinct = [
    If(i==k, True, Or(Not(Q[i][j]), Not(Q[k][j])))
    for k in range(n) for i in range(k)
    for j in range(n)
]
diag_distinct = [
    If(
        (i1+j1==i2+j2 or i1-j1==i2-j2) and i1 != i2,
        Or(Not(Q[i1][j1]), Not(Q[i2][j2])),
        True
    )
    for j1 in range(n) for j2 in range(n)
    for i2 in range(n) for i1 in range(i2)
]

time_start = time.process_time()
solve(row_exist + row_distinct + col_exist + col_distinct + diag_distinct)
time_end = time.process_time()
time_sum = time_end - time_start
print("solve time: ", time_sum)