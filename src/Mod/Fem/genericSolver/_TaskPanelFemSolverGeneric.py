# the task panel of the FemSolverGeneric (FreeCAD object)

import FreeCADGui
from PySide import QtGui
from genericSolver import solvers

text_field = QtGui.QFormLayout.LabelRole
input_field = QtGui.QFormLayout.FieldRole

class TaskPanelFemSolverGeneric:
    def __init__(self, solver_object):
        self.form = []
        self.base_widget = QtGui.QWidget()
        self.layout = QtGui.QFormLayout(self.base_widget)
        self.base_widget.setWindowTitle("generic solver")
        self.form += [self.base_widget]
        self.setupWidget()

    def setupWidget(self):
        # 1 list widget to select a "analyse type" (property of the solver object!)
        # 2 button to reload solvers necessary?
        # 3 write file button
        self.QwriteFile = QtGui.QPushButton("write file")
        self.QsolveCase = QtGui.QPushButton("solve case")
        self.QreloadSolvers = QtGui.QPushButton("reload solvers")
        self.QlistSolvers = QtGui.QComboBox()
        # self.layout.setWidget(0, text_field, QtGui.QLabel("analyse type")) # meabe a category
        self.layout.setWidget(1, text_field, self.QreloadSolvers)
        self.layout.setWidget(1, input_field, self.QlistSolvers)
        self.layout.setWidget(2, text_field, self.QwriteFile)
        self.layout.setWidget(2, input_field, self.QsolveCase)
        self.QlistSolvers.addItems(solvers.keys())

    def getStandardButtons(self):
        return int(QtGui.QDialogButtonBox.Close)

    def reject(self):
        FreeCADGui.ActiveDocument.resetEdit()
