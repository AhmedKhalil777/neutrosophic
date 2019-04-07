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
sys.path.append('src/neutrosophic_sets/single_valued')
# End of Directory Structure related Changes

from svnn import SingleValuedNeutrosophicNumber
from svnn_collection import SVNNCollection


class TestSingleNeutrosophicMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_set_characteristics(self):

        e1 = SingleValuedNeutrosophicNumber('E1', 0.001, 0, 0)
        e2 = SingleValuedNeutrosophicNumber('E2', 1, 0, 0)

        n_coll = SVNNCollection()
        n_coll.add_svnn(e1)
        n_coll.add_svnn(e2)

        weights = [0.9, 0.1]

        #self.assertEqual(n_coll.weighted_arithmetic_average(weights), (1,0,0))
        #self.assertEqual(n_coll.weighted_geometric_average(weights), (0.002, 0, 0))
        self.assertEqual(n_coll.ordered_weighted_arithmetic_average(weights), (1,0,0))
        self.assertEqual(n_coll.ordered_weighted_geometric_average(weights), (0.5012, 0, 0))



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
