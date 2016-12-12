__title__ = "_CommandSolverGeneric"
__url__ = "http://www.freecadweb.org"


import FreeCAD
import FreeCADGui
from FemCommands import FemCommands
from PySide import QtCore

import FemGui

class FemSolverGeneric(object):
    """The Fem::FemSolver's Proxy python type, add solver specific properties
    """
    solvers = {}
    def __init__(self, obj):
        self.Type = "Generic"
        self.Object = obj  # keep a ref to the DocObj for nonGui usage
        obj.Proxy = self  # link between App::DocumentObject to  this object

        obj.addProperty("App::PropertyString", "SolverType", "Base", "Type of the solver", 1)  # the 1 set the property to ReadOnly
        obj.SolverType = str(self.Type)

        obj.addProperty("App::PropertyPath", "WorkingDir", "Fem", "Working directory for calculations, will only be used it is left blank in preferences")
        # the working directory is not set, the solver working directory is only used if the preferences working directory is left blank


    def execute(self, obj):
        return

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state


class ViewProviderFemSolverGeneric(object):
    "A View Provider for the FemSolverCalculix object"
    def __init__(self, vobj):
        vobj.Proxy = self

    def getIcon(self):
        return ":/icons/fem-solver-generic.svg"

    def attach(self, vobj):
        self.ViewObject = vobj
        self.Object = vobj.Object

    def updateData(self, obj, prop):
        return

    def onChanged(self, vobj, prop):
        return

    def setEdit(self, vobj, mode=0):
        # TODO
        import _TaskPanelFemSolverGeneric
        taskd = _TaskPanelFemSolverGeneric.TaskPanelFemSolverGeneric(self.Object)
        FreeCADGui.Control.showDialog(taskd)
        return True

    def unsetEdit(self, vobj, mode=0):
        FreeCADGui.Control.closeDialog()
        return

    def doubleClicked(self, vobj):
        doc = FreeCADGui.getDocument(vobj.Object.Document)
        if not doc.getInEdit():
            # may be go the other way around and just activate the analysis the user has doubleClicked on ?!
            if FemGui.getActiveAnalysis() is not None:
                if FemGui.getActiveAnalysis().Document is FreeCAD.ActiveDocument:
                    if self.Object in FemGui.getActiveAnalysis().Member:
                        doc.setEdit(vobj.Object.Name)
                    else:
                        FreeCAD.Console.PrintError('Activate the analysis this solver belongs to!\n')
                else:
                    FreeCAD.Console.PrintError('Active Analysis is not in active Document!\n')
            else:
                FreeCAD.Console.PrintError('No active Analysis found!\n')
        else:
            FreeCAD.Console.PrintError('Active Task Dialog found! Please close this one first!\n')
        return True

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None






class _CommandSolverGeneric(FemCommands):
    "The Fem_SolverGeneric command definition"
    def __init__(self):
        super(_CommandSolverGeneric, self).__init__()
        self.resources = {'Pixmap': 'fem-solver-generic',
                          'MenuText': QtCore.QT_TRANSLATE_NOOP("Fem_SolverGeneric", "Solver Generic"),
                          'ToolTip': QtCore.QT_TRANSLATE_NOOP("Fem_SolverGeneric", "Creates a generic FEM solver")}
        self.is_active = 'with_analysis'

    def Activated(self):
        self.makeFemSolverGeneric()

    def makeFemSolverGeneric(self, name="Generic"):
        obj = FreeCAD.ActiveDocument.addObject("Fem::FemSolverObjectPython", name)
        FemSolverGeneric(obj)
        if FreeCAD.GuiUp:
            ViewProviderFemSolverGeneric(obj.ViewObject)
        return obj

FreeCADGui.addCommand('Fem_SolverGeneric', _CommandSolverGeneric())


class MyGenericSolver(object):
    pass

FemSolverGeneric.solvers["MyGenericSolver"] = MyGenericSolver