import unittest


class A(unittest.TestCase):

    def test_01(self):
        global b
        b = 2

    def test_02(self):
        if globals()["b"] == 2:
            self.skipTest("我是跳过用例的原因")
        print("pass")


if __name__ == "__main__":
    unittest.main()
