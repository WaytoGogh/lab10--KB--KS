# https://github.com/WaytoGogh/lab10--KB--KS
#Partner 1: Kai Belew
#Partner 2: Kezia Saint
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,-1), -2)
        self.assertEqual(add(0,0), 0)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,2,), 3)
        self.assertEqual(sub(0,3), -3)
        self.assertEqual(sub(-1, -2), 1)

    ##########################

    # Partner 1
    def test_multiply(self, a): # 3 assertions
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(a, list)
        # self.assertIsInstance(a, dict)
        # self.assertIsInstance(a, set)
        # self.assertIsInstance(a, tuple)
        # self.assertIsInstance(b, str)
        # self.assertIsInstance(b, list)
        # self.assertIsInstance(b, dict)
        # self.assertIsInstance(b, set)
        # self.assertIsInstance(b, tuple)
        self.assertEqual(mul(25, 2), 50)
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(10, 50), 500)

    def test_divide(self): # 3 assertions
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(a, list)
        # self.assertIsInstance(a, dict)
        # self.assertIsInstance(a, set)
        # self.assertIsInstance(a, tuple)
        # self.assertIsInstance(b, str)
        # self.assertIsInstance(b, list)
        # self.assertIsInstance(b, dict)
        # self.assertIsInstance(b, set)
        # self.assertIsInstance(b, tuple)
        self.assertEqual(mul(10, 50), 5)
        self.assertEqual(mul(10, 500), 50)
        self.assertEqual(mul(10, 20), 2)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100),2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**3),3)

    def test_log_invalid_base(self): # 1 assertion
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(a, list)
        # self.assertIsInstance(a, dict)
        # self.assertIsInstance(a, set)
        # self.assertIsInstance(a, tuple)
        # self.assertIsInstance(b, str)
        # self.assertIsInstance(b, list)
        # self.assertIsInstance(b, dict)
        # self.assertIsInstance(b, set)
        # self.assertIsInstance(b, tuple)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(a, list)
        # self.assertIsInstance(a, dict)
        # self.assertIsInstance(a, set)
        # self.assertIsInstance(a, tuple)
        # self.assertIsInstance(b, str)
        # self.assertIsInstance(b, list)
        # self.assertIsInstance(b, dict)
        # self.assertIsInstance(b, set)
        # self.assertIsInstance(b, tuple)
        self.assertAlmostEqual(hypotenuse(2, 3), 3.605)
        self.assertAlmostEqual(hypotenuse(10, 20), 22.361)
        self.assertAlmostEqual(hypotenuse(9, 45), 45.891)

    def test_sqrt(self): # 3 assertions
        # self.assertIsInstance(a, str)
        # self.assertIsInstance(a, list)
        # self.assertIsInstance(a, dict)
        # self.assertIsInstance(a, set)
        # self.assertIsInstance(a, tuple)
        # self.assertIsInstance(b, str)
        # self.assertIsInstance(b, list)
        # self.assertIsInstance(b, dict)
        # self.assertIsInstance(b, set)
        # self.assertIsInstance(b, tuple)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(144), 12.0)
        self.assertAlmostEqual(square_root(35), 5.916)
        self.assertAlmostEqual(square_root(71), 8.426)
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()