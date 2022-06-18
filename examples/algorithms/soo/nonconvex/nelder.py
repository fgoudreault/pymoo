from pymoo.algorithms.soo.nonconvex.nelder import NelderMead
from pymoo.problems import get_problem
from pymoo.optimize import minimize

problem = get_problem("sphere")

algorithm = NelderMead()

res = minimize(problem,
               algorithm,
               seed=1,
               verbose=True)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))