# """
# Naive backtracking search without any heuristics or inference
# """
# VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
# CONSTRAINTS = [
#     ("A", "B"),
#     ("A", "C"),
#     ("B", "C"),
#     ("B", "D"),
#     ("B", "E"),
#     ("C", "E"),
#     ("C", "F"),
#     ("D", "E"),
#     ("E", "F"),
#     ("E", "G"),
#     ("F", "G"),
# ]
#
#
# def backtrack(assignment):
#     """Runs backtracking search to find an assignment"""
#
#     # Check if assignment is complete
#     if len(assignment) == len(VARIABLES):
#         return assignment
#
#     # Try a new variable
#     var = select_unassigned_variable(assignment)
#     for value in ["Monday", "Tuesday", "Wednesday"]:
#         new_assignment = assignment.copy()
#         new_assignment[var] = value
#         if consistent(new_assignment):
#             result = backtrack(new_assignment)
#             if result is not None:
#                 return result
#     return None
#
#
# def select_unassigned_variable(assignment):
#     """Chooses a variable not yet assigned, in order"""
#     for variable in VARIABLES:
#         if variable not in assignment:
#             return variable
#     return None
#
#
# def consistent(assignment):
#     """Checks to see if an assignment is consistent"""
#     for (x, y) in CONSTRAINTS:
#
#         # only consider arcs where both are assigned
#         if x not in assignment or y not in assignment:
#             continue
#
#         # if both have same values, then not consistent
#         if assignment[x] == assignment[y]:
#             return False
#
#     # if nothing inconsistent, then assignment is consistent
#     return True
#
#
# solution = backtrack(dict())
# print(solution)
# try:
#     from constraint import *
# except ModuleNotFoundError:
#     print("Install the module Dude!!")
#
# problem = problem()
#
# # Add variables
# problem.addVariables(
#     ["A", "B", "C", "D", "E", "F", "G"],
#     ["Monday", "Tuesday", "Wednesday"]
# )
#
# # Add constraints
# CONSTRAINTS = [
#     ("A", "B"),
#     ("A", "C"),
#     ("B", "C"),
#     ("B", "D"),
#     ("B", "E"),
#     ("C", "E"),
#     ("C", "F"),
#     ("D", "E"),
#     ("E", "F"),
#     ("E", "G"),
#     ("F", "G"),
# ]
#
# for x, y in CONSTRAINTS:
#     problem.addConstraint(lambda x, y: x != y, (x, y))
#
# # solve problem
# for solution in problem.getSolution():
#     print(solution)


a = 4 > 3 > 2 > 1
print(a)