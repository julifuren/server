import yaml

with open('demo.yml', 'r', encoding='utf-8') as yaml_file:
    config_data = yaml.safe_load(yaml_file)

value1 = config_data

print(value1)


@file_data('demo.yaml')
def test_search5(self, case):
    search_key = case[0]["search_key"]
    print("第五组测试用例：", search_key)
    self.baidu_search(search_key)
    self.assertEqual(self.driver.title, search_key + "_百度搜索")
