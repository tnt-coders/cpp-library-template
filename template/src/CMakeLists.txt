tnt_project_AddLibrary(${PROJECT_NAME}
  TARGET
    ${PROJECT_NAME}
  SOURCES
    @name@.cpp
)

target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)