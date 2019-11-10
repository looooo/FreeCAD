# Python non Gui packages and modules
SET(FemScripts_SRCS
    coding_conventions.md
    __init__.py
    init.py
    init_gui.py
    objects_fem.py
    test_fem.py
    femgui.py  # should be added to gui install target
)

SET(FemCommands_SRCS
    commands/__init__.py
    commands/commands.py
    commands/manager.py
)

SET(FemExamples_SRCS
    examples/__init__.py
    examples/boxanalysis.py
    examples/ccx_cantilever_std.py
    examples/manager.py
    examples/material_multiple_twoboxes.py
    examples/material_nl_platewithhole.py
    examples/rc_wall_2d.py
    examples/thermomech_flow1d.py
    examples/thermomech_spine.py
)

SET(FemExampleMeshes_SRCS
    examples/meshes/__init__.py
    examples/meshes/mesh_boxanalysis_tetra10.py
    examples/meshes/mesh_boxes_2_vertikal_tetra10.py
    examples/meshes/mesh_canticcx_tetra10.py
    examples/meshes/mesh_rc_wall_2d_tria6.py
    examples/meshes/mesh_platewithhole_tetra10.py
    examples/meshes/mesh_thermomech_flow1d_seg3.py
    examples/meshes/mesh_thermomech_spine_tetra10.py
)

SET(FemInOut_SRCS
    inout/__init__.py
    inout/convert2TetGen.py
    inout/importCcxDatResults.py
    inout/importCcxFrdResults.py
    inout/importFenicsMesh.py
    inout/importInpMesh.py
    inout/importToolsFem.py
    inout/importVTKResults.py
    inout/importYamlJsonMesh.py
    inout/importZ88Mesh.py
    inout/importZ88O2Results.py
    inout/readFenicsXDMF.py
    inout/readFenicsXML.py
    inout/writeFenicsXDMF.py
    inout/writeFenicsXML.py
)

SET(FemMesh_SRCS
    mesh/__init__.py
    mesh/femmesh2mesh.py
    mesh/gmshtools.py
    mesh/meshtools.py
)

SET(FemResult_SRCS
    result/__init__.py
    result/resulttools.py
)

SET(FemSolver_SRCS
    solver/__init__.py
    solver/equationbase.py
    solver/report.py
    solver/reportdialog.py
    solver/run.py
    solver/settings.py
    solver/signal.py
    solver/solverbase.py
    solver/task.py
    solver/writerbase.py
)

SET(FemSolverCalculix_SRCS
    solver/calculix/__init__.py
    solver/calculix/solver.py
    solver/calculix/tasks.py
    solver/calculix/writer.py
)

SET(FemSolverElmer_SRCS
    solver/elmer/__init__.py
    solver/elmer/sifio.py
    solver/elmer/solver.py
    solver/elmer/tasks.py
    solver/elmer/writer.py
)

SET(FemSolverElmerEquations_SRCS
    solver/elmer/equations/__init__.py
    solver/elmer/equations/electrostatic.py
    solver/elmer/equations/elasticity.py
    solver/elmer/equations/equation.py
    solver/elmer/equations/flow.py
    solver/elmer/equations/fluxsolver.py
    solver/elmer/equations/heat.py
    solver/elmer/equations/linear.py
    solver/elmer/equations/nonlinear.py
)

SET(FemSolverFenics_SRCS
    solver/fenics/__init__.py
    solver/fenics/fenics_tools.py
)

SET(FemSolverZ88_SRCS
    solver/z88/__init__.py
    solver/z88/solver.py
    solver/z88/tasks.py
    solver/z88/writer.py
)

SET(FemTests_SRCS
    test/__init__.py
)

SET(FemTestsApp_SRCS
    test/app/__init__.py
    test/app/support_utils.py
    test/app/test_ccxtools.py
    test/app/test_common.py
    test/app/test_femimport.py
    test/app/test_material.py
    test/app/test_mesh.py
    test/app/test_object.py
    test/app/test_result.py
    test/app/test_solverframework.py
)

SET(FemTestsFiles_SRCS
    test/data/__init__.py
)

SET(FemTestsCcx_SRCS
    test/data/ccx/__init__.py
    test/data/ccx/cube_frequency.inp
    test/data/ccx/cube_frequency.dat
    test/data/ccx/cube_frequency.frd
    test/data/ccx/cube_frequency_expected_values
    test/data/ccx/cube_frequency.FCStd
    test/data/ccx/cube_static.inp
    test/data/ccx/cube_static.dat
    test/data/ccx/cube_static.frd
    test/data/ccx/cube_static_expected_values
    test/data/ccx/cube_static.FCStd
    test/data/ccx/cube.FCStd
    test/data/ccx/multimat.inp
    test/data/ccx/spine_thermomech.inp
    test/data/ccx/spine_thermomech.dat
    test/data/ccx/spine_thermomech.frd
    test/data/ccx/spine_thermomech_expected_values
    test/data/ccx/spine_thermomech.FCStd
    test/data/ccx/Flow1D_thermomech.inp
    test/data/ccx/Flow1D_thermomech.dat
    test/data/ccx/Flow1D_thermomech.frd
    test/data/ccx/Flow1D_thermomech_expected_values
    test/data/ccx/Flow1D_thermomech_inout_nodes.txt
    test/data/ccx/Flow1D_thermomech.FCStd
)

SET(FemTestsElmer_SRCS
    test/data/elmer/__init__.py
    test/data/elmer/case.sif
    test/data/elmer/group_mesh.geo
    test/data/elmer/ELMERSOLVER_STARTINFO
)

SET(FemTestsMesh_SRCS
    test/data/mesh/__init__.py
    test/data/mesh/tetra10_mesh.inp
    test/data/mesh/tetra10_mesh.unv
    test/data/mesh/tetra10_mesh.vtk
    test/data/mesh/tetra10_mesh.yml
    test/data/mesh/tetra10_mesh.z88
)

SET(FemTools_SRCS
    tools/__init__.py
    tools/ccxtools.py
    tools/femutils.py
)

SET(FemObjectsScripts_SRCS
    objects/__init__.py
    objects/_FemConstraintBodyHeatSource.py
    objects/_FemConstraintElectrostaticPotential.py
    objects/_FemConstraintFlowVelocity.py
    objects/_FemConstraintInitialFlowVelocity.py
    objects/_FemConstraintSelfWeight.py
    objects/_FemElementFluid1D.py
    objects/_FemElementGeometry1D.py
    objects/_FemElementGeometry2D.py
    objects/_FemElementRotation1D.py
    objects/_FemMaterial.py
    objects/_FemMaterialReinforced.py
    objects/_FemMaterialMechanicalNonlinear.py
    objects/_FemMeshBoundaryLayer.py
    objects/_FemMeshGmsh.py
    objects/_FemMeshGroup.py
    objects/_FemMeshRegion.py
    objects/_FemMeshResult.py
    objects/_FemResultMechanical.py
    objects/_FemSolverCalculix.py
    objects/FemConstraint.py
)

SET(FemAllScripts
    ${FemScripts_SRCS}
    ${FemCommands_SRCS}
    ${FemExamples_SRCS}
    ${FemExampleMeshes_SRCS}
    ${FemInOut_SRCS}
    ${FemMesh_SRCS}
    ${FemResult_SRCS}
    ${FemSolver_SRCS}
    ${FemSolverCalculix_SRCS}
    ${FemSolverElmer_SRCS}
    ${FemSolverElmerEquations_SRCS}
    ${FemSolverFenics_SRCS}
    ${FemSolverZ88_SRCS}
    ${FemTests_SRCS}
    ${FemTestsApp_SRCS}
    ${FemTestsFiles_SRCS}
    ${FemTestsCcx_SRCS}
    ${FemTestsElmer_SRCS}
    ${FemTestsMesh_SRCS}
    ${FemTools_SRCS}
    ${FemObjectsScripts_SRCS}
)


ADD_CUSTOM_TARGET(FemScriptsTarget ALL
    SOURCES ${FemAllScripts}
)

fc_copy_sources(FemScriptsTarget "${CMAKE_BINARY_DIR}/Ext/freecad/fem" ${FemAllScripts})


# install Python packages (for make install)
INSTALL(FILES ${FemScripts_SRCS} DESTINATION Ext/freecad/fem)
INSTALL(FILES ${FemCommands_SRCS} DESTINATION Ext/freecad/fem/commands)
INSTALL(FILES ${FemExamples_SRCS} DESTINATION Ext/freecad/fem/examples)
INSTALL(FILES ${FemExampleMeshes_SRCS} DESTINATION Ext/freecad/fem/examples/meshes)
INSTALL(FILES ${FemInOut_SRCS} DESTINATION Ext/freecad/fem/inout)
INSTALL(FILES ${FemMesh_SRCS} DESTINATION Ext/freecad/fem/mesh)
INSTALL(FILES ${FemResult_SRCS} DESTINATION Ext/freecad/fem/result)
INSTALL(FILES ${FemSolver_SRCS} DESTINATION Ext/freecad/fem/solver)
INSTALL(FILES ${FemSolverCalculix_SRCS} DESTINATION Ext/freecad/fem/solver/calculix)
INSTALL(FILES ${FemSolverElmer_SRCS} DESTINATION Ext/freecad/fem/solver/elmer)
INSTALL(FILES ${FemSolverElmerEquations_SRCS} DESTINATION Ext/freecad/fem/solver/elmer/equations)
INSTALL(FILES ${FemSolverFenics_SRCS} DESTINATION Ext/freecad/fem/solver/fenics)
INSTALL(FILES ${FemSolverZ88_SRCS} DESTINATION Ext/freecad/fem/solver/z88)
INSTALL(FILES ${FemTests_SRCS} DESTINATION Ext/freecad/fem/test)
INSTALL(FILES ${FemTestsApp_SRCS} DESTINATION Ext/freecad/fem/test/app)
INSTALL(FILES ${FemTestsFiles_SRCS} DESTINATION Ext/freecad/fem/test/data)
INSTALL(FILES ${FemTestsCcx_SRCS} DESTINATION Ext/freecad/fem/test/data/ccx)
INSTALL(FILES ${FemTestsElmer_SRCS} DESTINATION Ext/freecad/fem/test/data/elmer)
INSTALL(FILES ${FemTestsMesh_SRCS} DESTINATION Ext/freecad/fem/test/data/mesh)
INSTALL(FILES ${FemTools_SRCS} DESTINATION Ext/freecad/fem/tools)
INSTALL(FILES ${FemObjectsScripts_SRCS} DESTINATION Ext/freecad/fem/objects)



# Python Gui packages and modules
SET(FemGuiScripts_SRCS
    guiobjects/__init__.py
    guiobjects/_TaskPanelFemSolverControl.py
    guiobjects/_ViewProviderFemConstraintBodyHeatSource.py
    guiobjects/_ViewProviderFemConstraintElectrostaticPotential.py
    guiobjects/_ViewProviderFemConstraintFlowVelocity.py
    guiobjects/_ViewProviderFemConstraintInitialFlowVelocity.py
    guiobjects/_ViewProviderFemConstraintSelfWeight.py
    guiobjects/_ViewProviderFemElementFluid1D.py
    guiobjects/_ViewProviderFemElementGeometry1D.py
    guiobjects/_ViewProviderFemElementGeometry2D.py
    guiobjects/_ViewProviderFemElementRotation1D.py
    guiobjects/_ViewProviderFemMaterial.py
    guiobjects/_ViewProviderFemMaterialReinforced.py
    guiobjects/_ViewProviderFemMaterialMechanicalNonlinear.py
    guiobjects/_ViewProviderFemMeshBoundaryLayer.py
    guiobjects/_ViewProviderFemMeshGmsh.py
    guiobjects/_ViewProviderFemMeshGroup.py
    guiobjects/_ViewProviderFemMeshRegion.py
    guiobjects/_ViewProviderFemMeshResult.py
    guiobjects/_ViewProviderFemResultMechanical.py
    guiobjects/_ViewProviderFemSolverCalculix.py
    guiobjects/FemSelectionWidgets.py
    guiobjects/ViewProviderFemConstraint.py
)


if(BUILD_GUI)
    ADD_CUSTOM_TARGET(FemGuiScriptsTarget ALL
        SOURCES ${FemGuiScripts_SRCS}
    )
    fc_copy_sources(FemGuiScriptsTarget "${CMAKE_BINARY_DIR}/Ext/freecad/fem" ${FemGuiScripts_SRCS})

    # install Python packages (for make install)
    INSTALL(FILES ${FemGuiScripts_SRCS} DESTINATION Ext/freecad/fem/guiobjects)
endif(BUILD_GUI)
