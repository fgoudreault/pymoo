import numpy as np
from sklearn.utils import shuffle

from pymoo.core.population import Population
from pymoo.core.problem import Problem
from pymoo.operators.crossover.pcx import PCX
from pymoo.visualization.scatter import Scatter

X = np.array([[1, 0, 0], [0.9, 0.1, 0.1], [0, 0, 1]])
a, b, c = Population.new(X=X)

parents = [shuffle([a, b, c]) for _ in range(1000)]

pcx = PCX(eta=0.1, zeta=0.1)

Xp = pcx(Problem(n_var=3, xl=-1, xu=1), parents, to_numpy=True)

sc = Scatter()
sc.add(Xp, facecolor=None, edgecolor="blue", alpha=0.7)
sc.add(X, s=100, color="red")
sc.add(X.mean(axis=0), color="green", label="Centroid")
sc.show()
