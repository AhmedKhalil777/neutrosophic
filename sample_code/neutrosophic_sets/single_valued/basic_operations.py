# In the Name of ALLAH

import unittest
import os
import sys

# TODO Premature Optimization is the root of all evil
# Will work on a better way inchALLAH
# Don't touch the following lines right now
# Don't change the Directory structure
os.path.dirname(os.path.realpath(__file__))
os.chdir('..')
os.chdir('..')
os.chdir('..')
sys.path.append(os.getcwd())
sys.path.append('src/neutrosophic_set/single_valued')
# End of Directory Structure related Changes

def Example1():
    """From
    © Springer Nature Switzerland AG 2019
    C. Kahraman and İ. Otay (eds.), Fuzzy Multi-criteria Decision-Making
    Using Neutrosophic Sets, Studies in Fuzziness and Soft Computing 369,
    https://doi.org/10.1007/978-3-030-00045-5_2

    Page 3: Assume universe of discourse X = {x1, x2, x3} where
    - x1: characterizes capability
    - x2: characterizes worthiness
    - x3: characterizes prices of objects

    Assume that values of x1, x2, x3 are between [0,1]
    and they are obtained from some questionnaires of some experts.
    The experts may impose their opinion in three components viz. the degree of goodness,
    the degree of indeterminacy and that of poorness to explain the characterisof the objects.

    Suppose A is neutrosophic set: {<x1, (0.4, 0.7, 0.8)>, <x2, (0.5, 0.4, 0.3)>, <x3, (0.2, 0.4, 0.6)>}
    where the grade of goodness of capability is 0.4, grade of indeterminacy of capability is 0.7
    and grade of falsity of capability is 0.8

    So, how would we implement such an example using our Neutrosophic Package
    """
    # 1 - import NSet and Element modules
    from element import Element
    from nset import NSet

    # 2 - create the neutrosophic set
    nset_a = NSet()

    # 3 - create the elements
    x1 = Element('x1', 0.4, 0.7, 0.8)
    x2 = Element('x2', 0.5, 0.4, 0.3)
    x3 = Element('x3', 0.2, 0.4, 0.6)

    # 4 - add the elements to the neutrosophic set
    nset_a.add_element(x1)
    nset_a.add_element(x2)
    nset_a.add_element(x3)

    # 5 - print the set to make sure elements are added correctly
    print(nset_a)


if __name__ == '__main__':
    Example1()


