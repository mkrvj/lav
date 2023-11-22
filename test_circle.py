import unittest
import math
from circle import area, perimeter

class CircleleTestCase(unittest.TestCase):
    def test_zero1_mul(self):
       res = area(3)
       self.assertEqual(res, math.pi * 9) 

    def test_perimeter_1_mul(self):
       res = perimeter(5)
       self.assertEqual(res, math.pi * 10)
