# Proposal for a genric fem-solver

## goals

- a generic interface to connect any solver into the FEM Module of FreeCAD
- adding custom (specific) solvers at runtime
- find a generic way to satisfy most use-cases

## structure

#### freecad level
the generic solver is only one FreeCAD class. The solver type is set by choosing from a listproperty. At the moment I can't think of a usecase to implement another solver on FreeCAD-level. (maybe there is?)

#### python level
- GenericSolver
  - FenicsSolver
    - FenicsSteadyStateHeatSolver
    - FenicsHeatSolver *timedepending*
  - other solver types ...

#### GenericSolverApi

```python
class GenericSolver(object):
    def __init__(self, mesh, geo_properties):
        '''pass everything we need inside the solver'''

    def run(self):
        '''to be implemented by subclass'''

    def getSolution(self):
        '''to be implemented by subclass, called by freecad-solver after computation'''
```

#### Adding a new solver with the console:

```python
from Fem import GenericSolver
class mySolver(GenericSolver):
    ...

Fem.customSolvers.append(mySolver)
# maybe we should check if the solver is already in the list
# so doing it with a special function
Fem.registerSolver(mySolver)

```

## examples

### Heat equation with fenics

the steady state heat equation should be quite simple to implement and could be used as an example for the fenics solver class. To also deal with time depending analysis it makes sense to consider also an example for this use-case.

## Questions:

- How to pass the input data?
```python
mesh = {
    nodes: [...],
    elements: [...],
    element_groups: {name: [...]},
    node_groups: {name: [...]},
    element_properties: {group_name or element: {property_name: value}},
    node_properties: {group_name or node: {property_name: value}}}
```
- how to deal with solver options. How to pass them from the gui to the solver?
- generic property setter: Can we use there something from the fem-workbench?
- how to deal with time-depending analysis? Is the post-processing already useable for this?
