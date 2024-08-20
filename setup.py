from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize(
        ["solution_cy.pyx",
         "primes_cy.pyx",
         "primes_python_compiled.py"], 
         compiler_directives={"language_level": "3"},
         annotate=True,
         build_dir="build"
    ),
    include_dirs=[numpy.get_include()],
    script_args=['build'], 
                                            options={'build':{'build_lib':'.'}}
)