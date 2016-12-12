from PySide import QtCore

import FreeCADGui
import FreeCAD

from FemCommands import FemCommands
from genericSolver._FemSolverGeneric import FemSolverGeneric
from genericSolver._FemSolverGeneric import ViewProviderFemSolverGeneric


class CommandSolverGeneric(FemCommands):
    "The Fem_SolverGeneric command definition"
    def __init__(self):
        super(CommandSolverGeneric, self).__init__()
        self.resources = {'Pixmap': 'fem-solver-generic',
                          'MenuText': QtCore.QT_TRANSLATE_NOOP("Fem_SolverGeneric", "Solver Generic"),
                          'ToolTip': QtCore.QT_TRANSLATE_NOOP("Fem_SolverGeneric", "Creates a generic FEM solver")}
        self.is_active = 'with_analysis'

    def Activated(self):
        self.makeFemSolverGeneric()

    def makeFemSolverGeneric(self, name="Generic Solver"):
        obj = FreeCAD.ActiveDocument.addObject("Fem::FemSolverObjectPython", name)
        FemSolverGeneric(obj)
        if FreeCAD.GuiUp:
            ViewProviderFemSolverGeneric(obj.ViewObject)
        return obj


class CommandGenericProperty(FemCommands):
    "The Fem_GenericProperty command definition"
    def __init__(self):
        super(CommandGenericProperty, self).__init__()
        self.resources = {'Pixmap': 'fem-generic-property',
                          'MenuText': QtCore.QT_TRANSLATE_NOOP("Fem_GenericProperty", "generic properties"),
                          'ToolTip': QtCore.QT_TRANSLATE_NOOP("Fem_GenericProperty", "generic properties setter")}
        self.is_active = 'with_analysis'

    def Activated(self):
        # FreeCAD.ActiveDocument.openTransaction("Create GenericProperty")
        # FreeCADGui.addModule("FemGenericProperty")
        # FreeCADGui.doCommand("FemGui.getActiveAnalysis().Member = FemGui.getActiveAnalysis().Member + [FemGenericProperty.makeFemGenericProperty()]")
        # TODO
        pass


FreeCADGui.addCommand('Fem_SolverGeneric', CommandSolverGeneric())
FreeCADGui.addCommand('Fem_GenericProperty', CommandGenericProperty())
