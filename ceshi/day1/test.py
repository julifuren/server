import unittest
import ddt  # 导入ddt

# 测试数据
data = [
    {"phone": "dfasd132", "key": "dfabc"},
    {"phone": "dfsd134", "key": "dftest"},
    {"phone": "dfdfd188", "key": "dfmin"},
]


@ddt.ddt  # 声明我们要用它
class Test_ddt(unittest.TestCase):

    @ddt.file_data('demo.yml')
    def test_search5(self, aa):
        search_key = aa

        print(search_key)


if __name__ == '__main__':
    unittest.main()
