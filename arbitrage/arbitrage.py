# import numpy as np
from scipy.optimize import linprog

#           Yen       USD
# min -0.01 x_1 -0.08 x_2
c = [-0.01, -0.08]

# x_1 + x_2 <= 10000 (total asset)
#       x_2 <= 6000  (USD asset risk control)
A = [[1, 1], [0, 1]]
b = [10000, 6000]

# x > 0
x_bounds = (0, None)

resault = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method="highs")

if resault.success:
    print(f"Yen asset: {resault.x[0]:.2f}, USD asset: {resault.x[1]:.2f}")
    print(f"Prof: {-resault.fun:.2f}")
else:
    print("Failure")
