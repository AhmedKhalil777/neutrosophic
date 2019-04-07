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

from element import Element
from nset import NSet


class TestSingleNeutrosophicMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_set_characteristics(self):

        e1 = Element('E1', 0.25, 0.5, 0.25)
        e2 = Element('E2', 0.2, 0.25, 0.75)
        e3 = Element('E3', 0.35, 0.57, 0.45)
        e5 = Element('E3', 0.35, 0.57, 0.45)

        nset1 = NSet()
        nset2 = NSet()

        nset1.add_element(e1)
        self.assertEqual(len(nset1), 1)

        nset1.add_element(e2)
        self.assertEqual(len(nset1), 2)

        nset1.add_element(e3)
        self.assertEqual(len(nset1), 3)

        nset1.delete_element(e5._id)
        self.assertEqual(len(nset2), 0)

    def test_nset_subset_operation(self):

        e1 = Element('E1', 0.25, 0.5, 0.25)
        e2 = Element('E2', 0.2, 0.25, 0.75)
        e3 = Element('E3', 0.35, 0.57, 0.45)
        e5 = Element('E3', 0.35, 0.57, 0.45)

        nset1 = NSet()
        nset2 = NSet()

        nset1.add_element(e1)
        nset1.add_element(e2)
        nset1.add_element(e3)

        nset2.add_element(e5)

        self.assertTrue(nset2.subset_of(nset1))

        self.assertFalse(nset1.subset_of(nset2))

    def test_nset_equal_operation(self):

        e1 = Element('E1', 0.25, 0.5, 0.25)
        e2 = Element('E2', 0.2, 0.25, 0.75)
        e3 = Element('E3', 0.35, 0.57, 0.45)
        e5 = Element('E3', 0.35, 0.57, 0.45)

        nset1 = NSet()
        nset2 = NSet()

        nset1.add_element(e1)
        nset1.add_element(e2)
        nset1.add_element(e3)

        nset2.add_element(e5)

        self.assertFalse(nset2 == nset1)

        self.assertFalse(nset1 == nset2)

        nset2.add_element(e2)

        self.assertFalse(nset2 == nset1)

        self.assertFalse(nset1 == nset2)

        e4 = Element('E1', 0.25, 0.5, 0.25)
        nset2.add_element(e4)

        self.assertTrue(nset2 == nset1)

        self.assertTrue(nset1 == nset2)

    def test_nset_intersect_operation(self):

        e1 = Element('E1', 0.25, 0.5, 0.25)
        e2 = Element('E2', 0.2, 0.25, 0.75)
        e3 = Element('E3', 0.35, 0.57, 0.45)

        e4 = Element('E2', 0.4, 0.5, 0.5)
        e5 = Element('E3', 0.35, 0.57, 0.45)

        nset1 = NSet()
        nset2 = NSet()

#        nset1.add_element(e1)
        nset1.add_element(e2)
        nset1.add_element(e3)

        nset2.add_element(e5)
        nset2.add_element(e4)

        result_1 = nset1.intersect(nset2)
        result_2 = nset2.intersect(nset1)

        self.assertEqual(result_1, result_2)

        self.assertIn('E2', result_1)

        #self.assertNotIn('E3', result_1)

        print(result_1)
        #print(result_2)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
