from conans import ConanFile, CMake, tools

class Cpp@Name@(ConanFile):
    author = "TNT Coders <tnt-coders@googlegroups.com>"
    build_requires = "catch2/3.0.0@tnt-coders/testing"
    default_options = {"shared": False}
    description = "@description@"
    exports_sources = "CMakeLists.txt", "docs/*", "include/*", "src/*", "test/*"
    generators = "cmake", "cmake_paths"
    license = "GNU Lesser General Public License v3.0"
    name = "cpp-@name@"
    options = {"shared": [True, False]}
    settings = "os", "compiler", "build_type", "arch"
    topics = ("@name@")
    url = "https://github.com/tnt-coders/cpp-@name@"
    version = "0.0.0"

    def configure(self):
        tools.check_min_cppstd(self, "17")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake