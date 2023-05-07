import unittest

from calculator import add,subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
       self.assertEqual(add(1,2),3)
       self.assertEqual(add(3,2),5)
    def test_subtract(self):
       self.assertEqual(subtract(2,2),0)
       self.assertEqual(subtract(3,2),1) 
    def test_multiply(self):
       self.assertEqual(multiply(1,2),2)
       self.assertEqual(multiply(3,2),6) 
    def test_divide(self):
       self.assertEqual(divide(2,2),1)
       self.assertEqual(divide(4,0),2)   
       with self.assertRaises(ValueError):
          divide(1,0)

if __name__ == '__main__':
    unittest.main()


    
