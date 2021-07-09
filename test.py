import unittest
from tkinter import *
from for_testing import Calculate, calc
import math

class Test(unittest.TestCase):
    def test_normal(self):
        g = Calculate()
        g.input = "81 ÷ 9"

        self.assertEqual(g.button_equal(), 9 )

    def test_expo(self):
        g = Calculate()
        g.input = "2 ^ 2"

        self.assertEqual(g.button_equal(), 4)

    def test_expo2(self):
        g = Calculate()
        g.input = "2 ^ 3"

        self.assertEqual(g.button_equal(), 8)
    def test_expo3(self):
        g = Calculate()
        g.input = "4 ^ 0"

        self.assertEqual(g.button_equal(), 1)
    def test_expo4(self):
        g = Calculate()
        g.input = "4 ^ 2"

        self.assertEqual(g.button_equal(), 16)
    def test_expo5(self):
        g = Calculate()
        g.input = "4 ^ (-2)"

        self.assertEqual(g.button_equal(), 0.0625)
    def test_expo6(self):
        g = Calculate()
        g.input = "(-1) ^ 2"

        self.assertEqual(g.button_equal(), 1)
    def test_divide(self):
        g = Calculate()
        g.input = "4 ÷ 2"

        self.assertEqual(g.button_equal(), 2)
    def test_divide2(self):
        g = Calculate()
        g.input = "4 ÷ (-2)"

        self.assertEqual(g.button_equal(), -2)
    def test_divide3(self):
        g = Calculate()
        g.input = "(-4) ÷ (-2)"

        self.assertEqual(g.button_equal(), 2)
    def test_multi(self):
        g = Calculate()
        g.input = "4 x 0"

        self.assertEqual(g.button_equal(), 0)
    def test_multi2(self):
        g = Calculate()
        g.input = "4 x 4"

        self.assertEqual(g.button_equal(), 16)
    def test_multi3(self):
        g = Calculate()
        g.input = "1 x 4"

        self.assertEqual(g.button_equal(), 4)
    def test_multi4(self):
        g = Calculate()
        g.input = "4 x 5"

        self.assertEqual(g.button_equal(), 20)
    def test_multi5(self):
        g = Calculate()
        g.input = "5 x 5"

        self.assertEqual(g.button_equal(), 25)
    def test_multi6(self):
        g = Calculate()
        g.input = "(-5) x 5"

        self.assertEqual(g.button_equal(), -25)
    def test_add(self):
        g = Calculate()
        g.input = "10 + 10"

        self.assertEqual(g.button_equal(), 20)
    def test_add2(self):
        g = Calculate()
        g.input = "(-1) + 1"

        self.assertEqual(g.button_equal(), 0)
    def test_add3(self):
        g = Calculate()
        g.input = "(-1) + (-1)"

        self.assertEqual(g.button_equal(), -2)
    def test_subtract(self):
        g = Calculate()
        g.input = "10 - 5"

        self.assertEqual(g.button_equal(), 5)
    def test_subtract2(self):
        g = Calculate()
        g.input = "(-10) - 5"

        self.assertEqual(g.button_equal(), -15)
    def test_subtract3(self):
        g = Calculate()
        g.input = "(-1) - (-1)"

        self.assertEqual(g.button_equal(), 0)
    def test_pemdas(self):
        g = Calculate()
        g.input = "5*(5+3)+3-10/2"

        self.assertEqual(g.button_equal(), 38)

    def test_error(self):
        g = Calculate()
        g.input = "3+++"

        self.assertEqual(g.button_equal(), 'Syntax ERROR')
    def test_error2(self):
        g = Calculate()
        g.input = "3*/2"

        self.assertEqual(g.button_equal(), 'Syntax ERROR')
    def test_error3(self):
        g = Calculate()
        g.input = "3*/2"

        self.assertEqual(g.button_equal(), 'Syntax ERROR')
    def test_error4(self):
        g = Calculate()
        g.input = "dfghjkl;;o-"

        self.assertEqual(g.button_equal(), 'Syntax ERROR')
    def test_sin(self):
        g = Calculate()
        g.input = "math.sin(1)"

        self.assertEqual(g.button_equal(), 0.8414709848078965)
    def test_sin2(self):
        g = Calculate()
        g.input = "math.sin(-1)"

        self.assertEqual(g.button_equal(), -0.8414709848078965)
    def test_sin3(self):
        g = Calculate()
        g.input = "math.sin(0)"

        self.assertEqual(g.button_equal(), 0)
    def test_cos(self):
        g = Calculate()
        g.input = "math.cos(0)"

        self.assertEqual(g.button_equal(), 1)
    def test_cos2(self):
        g = Calculate()
        g.input = "math.cos(1)"

        self.assertEqual(g.button_equal(), 0.5403023058681398)
    def test_cos3(self):
        g = Calculate()
        g.input = "math.cos(-1)"

        self.assertEqual(g.button_equal(), 0.5403023058681398)
    def test_tan(self):
        g = Calculate()
        g.input = "math.tan(0)"

        self.assertEqual(g.button_equal(), 0)
    def test_tan2(self):
        g = Calculate()
        g.input = "math.tan(1)"

        self.assertEqual(g.button_equal(), 1.5574077246549023)
    def test_tan3(self):
        g = Calculate()
        g.input = "math.tan(-1)"

        self.assertEqual(g.button_equal(), -1.5574077246549023)
    def test_pi(self):
        g = Calculate()
        g.input = "math.pi * 1"

        self.assertEqual(g.button_equal(), 3.141592653589793 )
    def test_pi2(self):
        g = Calculate()
        g.input = "math.pi * 0"

        self.assertEqual(g.button_equal(), 0 )
    def test_pi3(self):
        g = Calculate()
        g.input = "math.pi * -1"

        self.assertEqual(g.button_equal(), -3.141592653589793 )
    def test_pi4(self):
        g = Calculate()
        g.input = "math.pi + 1"

        self.assertEqual(g.button_equal(), 4.141592653589793 )
    def test_pi5(self):
        g = Calculate()
        g.input = "math.pi - 1"

        self.assertEqual(g.button_equal(), 2.141592653589793 )

    def test_pi6(self):
        g = Calculate()
        g.input = "math.pi / 3"

        self.assertEqual(g.button_equal(), 1.0471975511965976)






if __name__ == "__main__":
    unittest.main()