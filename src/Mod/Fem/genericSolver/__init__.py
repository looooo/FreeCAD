import Fem
from genericSolver.GenericSolver import GenericSolver
import genericSolver._commands
from _FemSolverGeneric import FemSolverGeneric

solvers = {}

solvers["MyGenericSolver"] = GenericSolver
solvers["anotherSolver"] = GenericSolver

__all__ = ['FemSolverGeneric', 'GenericSolver']