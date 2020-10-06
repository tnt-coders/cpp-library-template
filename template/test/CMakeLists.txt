include(GoogleTest)

add_executable(@name@_test
    # TODO: <files>
    main.cpp
)

target_link_libraries(@name@_test
    @namespace@::@name@
    CONAN_PKG::gtest
)

gtest_discover_tests(@name@_test)