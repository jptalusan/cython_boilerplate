import numpy as np
import time
from solution import count_increases, count_increases_np
import primes, primes_python_compiled, primes_cy
import solution_cy

def test_count_increases():

    a = np.random.randint(0, 20000, 10000000)
    _a = list(a)
    
    start = time.time()
    i = count_increases(_a)
    elapsed = time.time() - start
    print("py:", elapsed)

    start = time.time()
    i = count_increases(a)
    elapsed = time.time() - start
    print("py1:", elapsed)

    start = time.time()
    i = count_increases_np(a)
    elapsed = time.time() - start
    print("py2:", elapsed)

    start = time.time()
    solution_cy.count_increases(_a)
    elapsed = time.time() - start
    print("cy1:", elapsed)

    start = time.time()
    solution_cy.count_increases_cy(_a)
    elapsed = time.time() - start
    print("cy2:", elapsed)

    start = time.time()
    solution_cy.count_increases_cy_array(a)
    elapsed = time.time() - start
    print("cy3:", elapsed)

def test_primes():
    primes_cy.primes(1000) == primes.primes(1000)
    primes_python_compiled.primes(1000) == primes.primes(1000)
    %%timeit
    primes.primes(1000)
    %%timeit
    primes_python_compiled.primes(1000)
    %%timeit
    primes_cy.primes(1000)


if __name__ == "__main__":
    test_count_increases()