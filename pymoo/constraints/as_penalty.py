from pymoo.core.individual import calc_cv
from pymoo.core.meta import Meta
from pymoo.core.problem import Problem, defaults_of_out
from pymoo.util.misc import from_dict

import numpy as np


class ConstraintsAsPenalty(Meta, Problem):

    def __init__(self,
                 problem,
                 penalty: float = 0.1):
        super().__init__(problem)

        # the amount of penalty to add for this type
        self.penalty = penalty

        # set ieq and eq to zero (because it became now a penalty)
        self.n_ieq_constr = 0
        self.n_eq_constr = 0

    def do(self, X, return_values_of, *args, **kwargs):

        out = self.__object__.do(X, return_values_of, *args, **kwargs)

        # get at the values from the output
        F, G, H = from_dict(out, "F", "G", "H")

        # store a backup of the values in out
        out["__F__"], out["__G__"], out["__H__"] = F, G, H

        # calculate the total constraint violation (here normalization shall be already included)
        CV = np.array([calc_cv(g, h) for g, h in zip(G, H)])

        # set the penalized objective values
        out["F"] = F + self.penalty * CV

        DEFAULTS = defaults_of_out(self, len(X))
        out["G"] = DEFAULTS["G"]()
        out["H"] = DEFAULTS["H"]()

        return out
