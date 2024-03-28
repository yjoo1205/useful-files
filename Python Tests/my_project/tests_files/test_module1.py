import unittest
from my_project.module1 import my_function

class TestMyFunction(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(my_function(2, 3), 5)
        
if __name__ == '__main__':
    unittest.main()