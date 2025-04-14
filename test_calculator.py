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
    def test_multiply(self): # 3 assertions
        self.assert isinstance(a, str)
        self.assert isinstance(a, list)
        self.assert isinstance(a, dict)
        self.assert isinstance(a, set)
        self.assert isinstance(a, tuple)
        self.assert isinstance(b, str)
        self.assert isinstance(b, list)
        self.assert isinstance(b, dict)
        self.assert isinstance(b, set)
        self.assert isinstance(b, tuple)
        self.assertEqual(mul(25, 2), 50)
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(10, 50), 500)

    def test_divide(self): # 3 assertions
        self.assert isinstance(a, str)
        self.assert isinstance(a, list)
        self.assert isinstance(a, dict)
        self.assert isinstance(a, set)
        self.assert isinstance(a, tuple)
        self.assert isinstance(b, str)
        self.assert isinstance(b, list)
        self.assert isinstance(b, dict)
        self.assert isinstance(b, set)
        self.assert isinstance(b, tuple)
        self.assertEqual(mul(10, 50), 5)
        self.assertEqual(mul(10, 500), 50)
        self.assertEqual(mul(10, 20), 2)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(10, 100),2)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(math.e, math.e**3),3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()