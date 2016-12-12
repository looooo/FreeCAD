import Fem
from genericSolver._GenericSolver import GenericSolver
import genericSolver._commands
from _FemSolverGeneric import FemSolverGeneric

solvers = {}

solvers["MyGenericSolver"] = GenericSolver

__all__ = ['FemSolverGeneric', 'GenericSolver']