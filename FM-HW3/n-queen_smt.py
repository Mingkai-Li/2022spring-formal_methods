from z3 import *
import time

n = int(input("n:"))
Q = [Int('Q_%i' % (i+1)) for i in range(n)]
val_c = [And(1 <= Q[i], Q[i] <= n) for i in range(n)]
col_c = [Distinct(Q)]
diag_c = [
    If(i==j, True, And(i+Q[i] != j+Q[j], i+Q[j] != j+Q[i]))
    for i in range(n) for j in range(i)
]

time_start = time.process_time()
solve(val_c + col_c + diag_c)
time_end = time.process_time()
time_sum = time_end - time_start
print("solve time: ", time_sum)