tnt_project_AddLibrary(${PROJECT_NAME}
  TARGET
    @name@
  SOURCES
    @name@.cpp
)

target_compile_features(@name@ PUBLIC cxx_std_17)