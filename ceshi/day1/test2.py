import unittest


class TestDemo(unittest.TestCase):

    def test_01(self):
        try:
            a = '测试用例1'
            b = 1
            self.assertEqual(a, '测试用例2')

        except:
            print('测试用例1失败')
            raise

    # @unittest.skipIf(test_case1.__doc__ == "用例1执行失败", "用例1未通过，跳过用例2")
    # @unittest.skipIf(test_01.__doc__ == '测试用例1' , 'reason')
    def test_02(self):
        # print(self.test_01.__doc__)
        try:
            a = 1
            b = 1
            self.assertEqual(a, b)

        except:
            print('用例失败')
            raise


if __name__ == '__main__':
    unittest.TestCase()
