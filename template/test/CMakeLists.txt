include(Catch)

add_executable(@name@_test
    # TODO: <files>
    main.cpp
)

target_link_libraries(@name@_test
    @namespace@::@name@
    Catch2::Catch2WithMain
)

gtest_discover_tests(@name@_test)