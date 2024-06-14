import scipy.optimize

"""Machine x1 and x2 , x1 costs $50/hr to run and x2 cost $80/hr to run.
Goal is to minimize cost. 
constraint 1
x1 requires 5 units of labour per hour. x2 requires 2 unit 
of labour per hour. total of 20units of labour to spend
Constraint 2
x1 produces 10 units of output per hour. x2 produces 12 units of output per hour.
company needs 90 units of output"""

# objective function : 50x_1 + 80x_2
# Constraint 1: 5x_1 + 2x_2 <= 20
# Constraint 2: -10x_1 + -12x_2 <= -90
try:
    result = scipy.optimize.linprog(
        [50, 80],  # Cost function: 50x_1 + 80x_2
        A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
        b_ub=[20, -90],  # Constraints for inequalities: 20 and -90

    )

    if result.success:
        print(f"X1:{round(result.x[0], 2)} hours")
        print(f"X2:{round(result.x[1], 2)} hours")

    else:
        print("Not solution")
except Exception as E:
    print(E)
