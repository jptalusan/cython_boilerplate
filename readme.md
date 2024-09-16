# Cython
## Steps
0. I used python3.11.
1. `pip install cython`
2. Build the cython code
  * `python setup.py build_ext --inplace`
  * Which will leave a file in your local directory called helloworld.so in unix or helloworld.pyd in Windows. Now to use this file: start the python interpreter and simply import it as if it was a regular python module:
    ```
    import helloworld
    ```
  Congratulations! You now know how to build a Cython extension. But so far this example doesn’t really give a feeling why one would ever want to use Cython, so lets create a more realistic example.

For more information on how Cython works and how you build it, look at the references below.
Main idea is, if you design your code to use pure python and numpy, you are already getting more efficient code any regular python code so the savings from usig Cython is minimal at best.

## References
* https://cython.readthedocs.io/en/stable/src/tutorial/cython_tutorial.html
* https://www.peterbaumgartner.com/blog/intro-to-just-enough-cython-to-be-useful/
* https://pandas.pydata.org/docs/user_guide/enhancingperf.html#cython-writing-c-extensions-for-pandas
