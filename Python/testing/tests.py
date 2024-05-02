import unittest
import to_test
# more: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class Test(unittest.TestCase):

    def test_floor_dev(self):
        self.assertEqual(to_test.floor_div(2, 3), 0)
        self.assertEqual(to_test.floor_div(10, 3), 3)
        self.assertEqual(to_test.floor_div(-3, 3), -1)
        self.assertRaises(ZeroDivisionError, to_test.floor_div, -3, 0)

# more: on mocks and classes: https://youtu.be/6tNS--WetLI?si=iznHhKnsmkCdmdQU&t=1699