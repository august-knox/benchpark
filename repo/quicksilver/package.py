# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Quicksilver(MakefilePackage):
    """Quicksilver is a proxy application that represents some elements of the
    Mercury workload.
    """

    tags = ["proxy-app"]

    homepage = "https://codesign.llnl.gov/quicksilver.php"
    #url = "https://github.com/LLNL/Quicksilver/tarball/V1.0"
    #git = "https://github.com/LLNL/Quicksilver.git"
    git = "https://github.com/august-knox/Quicksilver.git"
    maintainers("richards12")

    #version("master", branch="master")
    version("fixedCompilers", branch="gcc13+")
    version("1.0", sha256="83371603b169ec75e41fb358881b7bd498e83597cd251ff9e5c35769ef22c59a")

    variant("openmp", default=False, description="Build with OpenMP support")
    variant("O0", default=False, description="O0")
    variant("O2", default=False, description="O2")
    variant("O3", default=False, description="O3")
    variant("Os", default=False, description="Os")
    variant("mpi", default=False, description="Build with MPI support")
    variant("cuda", default=False, description="Build with CUDA support")
    depends_on("mpi", when="+mpi")

    build_directory = "src"

    @property
    def build_targets(self):
        targets = []
        spec = self.spec
        if "+mpi" in spec:
            targets.append("CXX={0}".format(spec["mpi"].mpicxx))
        else:
            targets.append("CXX={0}".format(spack_cxx))

        if "+openmp+mpi" in spec:
            targets.append("CPPFLAGS=-DHAVE_MPI -DHAVE_OPENMP {0}".format(self.compiler.openmp_flag))
        elif "+openmp" in spec:
            targets.append("CPPFLAGS=-DHAVE_OPENMP {0}".format(self.compiler.openmp_flag))
        elif "+mpi" in spec:
            targets.append("CPPFLAGS=-DHAVE_MPI")
        if "+openmp" in self.spec:
            targets.append("LDFLAGS={0}".format(self.compiler.openmp_flag))

        return targets

    def edit(self, spec, prefix):
        makefile = FileFilter("src/Makefile")
        if "+O0" in spec:
            makefile.filter('CXXFLAGS =', 'CXXFLAGS= -g -O0' )
        
        if "+O2" in spec:
            makefile.filter('CXXFLAGS =', 'CXXFLAGS= -g -O2' )

        if "+O3" in spec:
            makefile.filter('CXXFLAGS =', 'CXXFLAGS= -g -O3' )

        if "+Os" in spec:
            makefile.filter('CXXFLAGS =', 'CXXFLAGS= -g -Os' )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.doc)
        install("src/qs", prefix.bin)
        #install("src/Makefile", prefix.bin)
        install("LICENSE.md", prefix.doc)
        install("README.md", prefix.doc)
        install_tree("Examples", prefix.Examples)
