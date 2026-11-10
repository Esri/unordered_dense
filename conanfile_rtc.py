from conans import ConanFile

class UnorderedDense(ConanFile):
    name = "unordered_dense"
    version = "4.9.2"
    url = "https://github.com/Esri/unordered_dense/tree/runtimecore"
    license = "https://github.com/Esri/unordered_dense/blob/runtimecore/LICENSE"
    description = (
        "A fast & densely stored hashmap and hashset based on robin-hood backward shift deletion."
    )

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/unordered_dense/"

        # headers
        self.copy("*.h", src=base + "include/ankerl", dst=relative + "include/ankerl")
