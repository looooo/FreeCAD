import numpy as np
import FreeCADGui
import FreeCAD
from genericSolver import GenericSolver
import fenics

class FenicsSolver(GenericSolver):
    topology_dimension = 2 # 1=edges, 2=faces, 3=volumes
    geometry_dimension = 2 # 1=1d, 2=2d, 3=3d
    def __init__(self):
        super(FenicsSolver, self).__init__()
        self.fenics = __import__("fenics")

    def prepare(self):
        self.mesh = self.fenics.Mesh()
        editor = self.fenics.MeshEditor()
        editor.open(self.mesh, self.topology_dimension, self.geometry_dimension)
        editor.init_vertices(len(self.nodes))
        editor.init_cells(len(self.elements))
        for i, vert in enumerate(self.nodes):
            if self.geometry_dimension == 2:
                editor.add_vertex(i, np.array(vert[:-1]))
            else:
                editor.add_vertex(i, np.array(vert))
        for i, el in enumerate(self.elements):
            editor.add_cell(i, np.array(el, dtype=np.uintp))
        editor.close()
