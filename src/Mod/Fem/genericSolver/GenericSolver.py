# this is the base class for solvers pluged into the genericSolver interface.

# TODO: logger to see what was going wrong with the case


import time
from PySide import QtCore


class GenericSolver(object):

    def __init__(self):
        '''pass everything we need inside the solver'''
        self.set_properties = False
        self.nodes = []
        self.elements = []
        self.worker = QtCore.QThread()

    def doJob(self, foo, foo_start=None, foo_end=None):
        if not self.worker.isRunning():
            self.worker = QtCore.QThread()
            self.worker.run = foo
            if foo_start:
                self.worker.started.connect(foo_start)
            if foo_end:
                self.worker.finished.connect(foo_end)
            self.worker.start()
        else:
            raise RuntimeError("worker has job, please wait")

    def setMesh(self, nodes, elements):
        self.nodes = nodes
        self.elements = elements

    def setProperties(self, properties):
        pass

# function called in an extern thread
    def prepare(self):
        '''to be implemented by subclass'''
        pass

    def run(self):
        '''to be implemented by subclass'''
        time.sleep(5)

    def writeMesh(self, filename):
        '''to be implemented by subclass'''
        pass
######################################################

    def writeInputFile(self):
        pass

    def writeOutputFile(self):
        pass

    @property
    def typeOfElements(self):
        return "faces"