import numpy as np
import FreeCADGui
import FreeCAD

import sys
sys.stdout.isatty()
FreeCADGui.doCommand("import fenics")
# import fenics
from genericSolver import GenericSolver


class FenicsSolver(GenericSolver):
    topology_dimension = 2 # 1=edges, 2=faces, 3=volumes
    geometry_dimension = 2 # 2=2d, 3=3d

    def setMesh(self, vertices, elements):
        self.mesh = fenics.Mesh()
        editor = fenics.MeshEditor()
        editor.open(self.mesh, self.topology_dimension, self.geometry_dimension)
        editor.init_vertices(len(vertices))
        editor.init_cells(len(elements))
        for i, vert in enumerate(vertices):
            editor.add_vertex(i, np.array(vert))
        for i, el in enumerate(elements):
            editor.add_cell(i, *el)
        editor.close()

    