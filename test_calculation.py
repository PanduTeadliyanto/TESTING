#test_calculation
import unittest
from calculation import add, subtract

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(add(3, 1), 2)
        self.assertEqual(add(5, 2), 3)
        self.assertEqual(add(10, 3), 7)
    
    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add(1, '2')
            add('1', 2)
    
    if__name__== '__main__'
    unittest.main()