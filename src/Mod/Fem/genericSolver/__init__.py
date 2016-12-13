import Fem
from genericSolver.GenericSolver import GenericSolver
from genericSolver.FenicsSolver import FenicsSolver
import genericSolver._commands
from _FemSolverGeneric import FemSolverGeneric

solvers = {}

solvers["MyGenericSolver"] = GenericSolver
solvers["FenicsSolver"] = FenicsSolver

__all__ = ['FemSolverGeneric', 'GenericSolver']