import unittest
import os
import json

import things_to_test.functions as f

TEST_DIR = os.path.dirname(__file__)
IFILE_PATH = os.path.join( TEST_DIR, "data/inputs.json") 

class TestAdder(unittest.TestCase):

    def setUp(self):
        self.ifile = open(IFILE_PATH, "r")
        data = json.load(self.ifile)
        self.integers = data["Integers"]
        self.floats = data["Floats"]

    def tearDown(self):
        self.ifile.close()

    def test_integers(self):
        inputs = 1,2
        solution = 3
        result = f.adder(*inputs)
        self.assertEqual(result, solution)

    def test_floats(self):
        inputs = 1.2, 2.3
        solution = 3.5
        result = f.adder(*inputs)
        self.assertTrue(result == solution)

    def test_strings(self):
        inputs = "Hello", " World"
        solution = "Hello World"
        result = f.adder(*inputs)
        self.assertFalse(result != solution)

    def test_type_error(self):
        inputs = "string", 1
        error = TypeError
        with self.assertRaises(error):
            result = f.adder(*inputs)

    def test_loaded_data(self):
        inputs = self.integers[:2]
        solution = 3
        result = f.adder(*inputs)
        self.assertEqual(result, solution)

        inputs = self.floats[:2]
        solution = 0.3
        sig_figs = 10
        result = f.adder(*inputs)
        self.assertAlmostEqual(result, solution, sig_figs)


if __name__ == '__main__':
     unittest.main()
