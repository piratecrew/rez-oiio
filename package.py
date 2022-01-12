name = "oiio"

version = "2.3.11.0"

private_build_requires = [
    "pybind11-2"
]

requires = [
    "boost-1.76",
    "openexr-3",
    "ocio-2",
    "jpegturbo-2",
    "libpng-1",
]

@early()
def build_requires():
    # check if the system gcc is too old <9
    # then we require devtoolset-9
    requirements = ["cmake-3.15+<4"]
    from subprocess import check_output
    gcc_major = int(check_output(r"gcc -dumpversion | cut -f1 -d.", shell=True).strip().decode())
    if gcc_major < 9:
        requirements.append("devtoolset-9")

    return requirements

variants = [
    ["platform-linux", "python-3.7", "libraw-0"],
    ["platform-linux", "python-3.7", "libraw-master"]
]

build_command = "make -f {root}/Makefile {install}"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PYTHONPATH.append(
        "{root}/lib64/python{resolve.python.version.major}.{resolve.python.version.minor}/site-packages"
    )
