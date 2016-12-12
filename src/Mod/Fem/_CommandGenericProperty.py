__title__ = "_CommandGenericProperty"
__url__ = "http://www.freecadweb.org"


import FreeCAD
import FreeCADGui
from FemCommands import FemCommands
from PySide import QtCore


class _CommandGenericProperty(FemCommands):
    "The Fem_GenericProperty command definition"
    def __init__(self):
        super(_CommandGenericProperty, self).__init__()
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

FreeCADGui.addCommand('Fem_GenericProperty', _CommandGenericProperty())
