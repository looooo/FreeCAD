# the task panel of the FemSolverGeneric (FreeCAD object)

import time
from PySide import QtGui, QtCore
import FreeCAD
import FreeCADGui
import FemGui
from genericSolver import solvers
from genericSolver.FemToolsGeneric import FemToolsGeneric

from threading import Thread

text_field = QtGui.QFormLayout.LabelRole
input_field = QtGui.QFormLayout.FieldRole


class TaskPanelFemSolverGeneric:
    def __init__(self, solver_object):
        self.form = []
        self._solver = None
        self.console_message = ""
        self.mesh = None
        self.properties = {}
        self.start = 0
        self.object = solver_object
        self.current_thread = None

        self.setupMeshAndProperties()

        self.FemToolsGeneric = FemToolsGeneric()

        self.base_widget = QtGui.QWidget()
        self.layout = QtGui.QVBoxLayout(self.base_widget)
        self.base_widget.setWindowTitle("generic solver")
        self.form += [self.base_widget]
        self.setupWidget()

    def setupMeshAndProperties(self):
        for member in self.analysis.Member:
            if member.isDerivedFrom("Fem::FemMeshObject"):
                self.mesh = member


        if not self.mesh:
            raise(AttributeError("no mesh in analyse"))


    def setupWidget(self):
        # 1 list widget to select a "analyse type" (property of the solver object!)
        # 2 button to reload solvers necessary?
        # 3 write file button
        self.QwriteFile = QtGui.QPushButton("write file")
        self.QsolveCase = QtGui.QPushButton("solve case")
        self.QlistSolvers = QtGui.QComboBox()
        self.QtextOutput = QtGui.QTextEdit()
        self.QprepareMesh = QtGui.QPushButton("prepare mesh")
        # self.layout.setWidget(0, text_field, QtGui.QLabel("analyse type")) # meabe a category
        self.layout.addWidget(self.QlistSolvers)
        self.layout.addWidget(self.QprepareMesh)
        self.layout.addWidget(self.QwriteFile)
        self.layout.addWidget(self.QsolveCase)
        self.layout.addWidget(self.QtextOutput)
        self.QlistSolvers.addItems(solvers.keys())

        self.QprepareMesh.clicked.connect(self.prepare)
        self.QsolveCase.clicked.connect(self.solve)

    @property
    def solver(self):
        if not self._solver:
            solver_str = self.QlistSolvers.currentText()
            solver_class = solvers[solver_str]
            self._solver  = solver_class()
            self.QlistSolvers.setDisabled(True)
        return self._solver

    def prepare(self):
        self.solver.setMesh(*self.mesh2py()) 

        def write_finished():
            self.femConsoleMessage("end of preparation")

        def write_start():
            self.start = time.time()
            self.femConsoleMessage("start of preparation")

        self.solver.doJob(self.solver.prepare, write_start, write_finished)

    def solve(self):
        def write_finished():
            self.femConsoleMessage("end of computation")

        def write_start():
            self.start = time.time()
            self.femConsoleMessage("start of computation")

        self.solver.doJob(self.solver.run, write_start, write_finished)

    def _solve(self):
        pass
        # create a result object
        # result = FreeCAD.ActiveDocument.addObject('Fem::FemResultObject', "result")
        # result.Mesh = self.mesh
        # result.DisplacementLengths = solution
        # self.analysis.Member += [result]

    def mesh2py(self):
        # at this point the solver must be specified. Maybe another interface where the type of
        # solver is selected at the initialization of the solver is better?
        # also there are analysis types where faces and volumes are involved. How to deal with that?
        #   (I will leave this to others as this is I have no usecase for this at the moment.)

        # TODO passing groups of elements???

        elements = []
        if self._solver.typeOfElements == "volumes":
            for i in self.mesh.FemMesh.Volumes:
                elements.append(self.mesh.FemMesh.getElementNodes(i))
        elif self._solver.typeOfElements == "faces":
            for i in self.mesh.FemMesh.Faces:
                elements.append(list(self.mesh.FemMesh.getElementNodes(i)))
        elif self._solver.typeOfElements == "edges":
            pass  # TODO
        elements = [[(index - 1) for index in element] for element in elements]
        nodes = [list(i) for i in self.mesh.FemMesh.Nodes.values()]

        return nodes, elements

    def femConsoleMessage(self, message="", color="#000000"):
        # borrowed from calculix taskpanel, very nice
        self.console_message += '<font color="#0000FF">{0:4.1f}:\
                                     </font> <font color="{1}">{2}\
                                     </font><br>'.format(
                                     time.time() - self.start, color,
                                     message.encode('utf-8', 'replace'))
        self.QtextOutput.setText(self.console_message)
        self.QtextOutput.moveCursor(QtGui.QTextCursor.End)

    @property
    def analysis(self):
        if FemGui.getActiveAnalysis() is not None:
            if FemGui.getActiveAnalysis().Document is FreeCAD.ActiveDocument:
                if self.object in FemGui.getActiveAnalysis().Member:
                    return FemGui.getActiveAnalysis()
        raise(AttributeError("not member of analyse"))

    def getStandardButtons(self):
        return int(QtGui.QDialogButtonBox.Close)

    def reject(self):
        FreeCADGui.ActiveDocument.resetEdit()
