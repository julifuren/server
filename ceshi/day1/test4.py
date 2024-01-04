import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.test_case1_passed = True

    def test_case1(self):
        """
        用例1：这个测试用例应该失败。
        """
        result = False  # 模拟一个失败的测试用例
        self.assertFalse(result, "用例1执行失败")
        self.test_case1_passed = False  # 设置标志为 False

    @unittest.skipIf(self.test_case1_passed, "如果用例1失败，则跳过用例2")
    def test_case2(self):
        """
        用例2：这个测试用例依赖于用例1的成功。
        """
        if self.test_case1_passed:
            # 只有在用例1通过的情况下才会执行这段代码
            print("执行用例2")
        else:
            print("用例1执行失败，跳过用例2")


if __name__ == '__main__':
    unittest.main()
