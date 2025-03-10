# YAML 文件处理
# Python 中，可以使用第三方模块 PyYAML 来处理 YAML 文件。

# 安装 PyYAML 模块
# pip install pyyaml


# 读取 YAML 文件
# YAML 模块使用 safe_load() 方法读取 yaml 文件，在读取文件之前，和普通文件一样，需要先将文件打开。
import yaml


def read_yaml():
    with open('yaml_demo1.yaml', 'r', encoding='utf-8') as file:
        # 将文件内容读取到 data 变量中
        data = yaml.safe_load(file)
        return data


# 写入 YAML 文件
# YAML 模块使用 safe_dump() 方法向 yaml 文件中写入数据，在写入文件之前，也需要先将文件打开。
def write_yaml():
    # 创建一个字典
    data = {
        'name': 'test',
        'age': 18,
        'hard_list': [
            {
                'test': [1, 2, 3]
            },
            {
                'test': [4, 5, 6]
            }
        ]
    }
    with open('yaml_demo2.yaml', 'w', encoding='utf-8') as file:
        # 将字典写入到文件中
        yaml.safe_dump(data, file)


if __name__ == '__main__':
    result = read_yaml()
    print(result)
    # 获取嵌套列表中的值
    print(result['hard_list'][2]['test'][1])
    write_yaml()
