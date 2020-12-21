include(Catch)

add_executable(${PROJECT_NAME}_test
    # TODO: <files>
    main.cpp
)

target_link_libraries(${PROJECT_NAME}_test
    @namespace@::${PROJECT_NAME}
    Catch2::Catch2WithMain
)

gtest_discover_tests(${PROJECT_NAME}_test)