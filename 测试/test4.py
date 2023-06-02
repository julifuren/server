import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    # 测试用例前置动作
    def setUp(self):
        print("test start:")

    # 测试用例后置动作
    def tearDown(self):
        print("test end")

    def test_add(self):
        c = Calculator(3, 5)

    result = c.add()
    self.assertEqual(result, 8)

    def test_sub(self):
        c = Calculator(7, 2)

    result = c.sub()
