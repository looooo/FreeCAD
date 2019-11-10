SET(PY_SRC
    femcommands.py
    femexamples.py
    femguiobjects.py
    feminout.py
    femmesh.py
    femobjects.py
    femresult.py
    femsolver.py
    femtest.py
    femtools.py
    ObjectsFem.py
    TestFem.py
    )

ADD_CUSTOM_TARGET(DeprecatedScriptsTarget ALL
    SOURCES ${PY_SRC}
)

fc_copy_sources(DeprecatedScriptsTarget "${CMAKE_BINARY_DIR}/Mod/Deprecated" ${PY_SRC})


# install Python packages (for make install)
INSTALL(FILES ${PY_SRC} DESTINATION Mod/Deprecated)