# this is the base class for solvers pluged into the genericSolver interface.

class GenericSolver(object):
    def __init__(self):
        '''pass everything we need inside the solver'''
        self.set_properties = False
        self.nodes = []
        self.elements = []

    def setMesh(self, nodes, elements):
        self.nodes = nodes
        self.elements = elements
        print(self.elements)

    def setProperties(self, properties):
        pass

    def run(self):
        '''to be implemented by subclass'''
        pass

    def getSolution(self):
        '''to be implemented by subclass, called by freecad-solver after computation'''
        pass

    def convertMesh(self):
        '''implement by subclass'''
        pass

    def convertBCs(self):
        '''implement by subclass'''
        pass

    def writeMesh(self, filename):
        '''writes the mesh to file'''
        pass

    def writeInputFile(self):
        pass

    def writeOutputFile(self):
        pass

    @property
    def typeOfElements(self):
        return "faces"