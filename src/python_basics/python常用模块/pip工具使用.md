# pip 工具使用
## 简介
*pip* 是 *Python* 中用于管理第三方包的工具。
他可以帮助下载、安装、升级和管理各种 *Python* 包，能够轻松的引入外部库和模块到项目中。

## pip常用命令
| 功能       | 指令                       |
|:---------|:-------------------------|
| 查看pip 版本 | pip -V                   |
| 查看帮助文档   | pip help                 |
| 查看包列表    | pip list                 |
| 安装       | pip install 包名           |
| 升级       | pip install --upgrade 包名 |
| 卸载       | pip uninstall 包名         |


## pip 安装包
- 普通安装


```shell
# 默认安装最新版本
pip install pytest
```

- 指定版本安装
```shell
# 指定版本
pip install pytest==6.2.0
```

- 批量安装
```shell
# 从文件清单中批量安装
pip install -r requirments.txt

# 文件格式
pytest==6.2.0
Faker==9.3.1
selenium==3.14.1
```

## pip 升级包
```shell
pip install --upgrade 包名
```

## pip 卸载包
```shell
pip uninstall 包名
```

## pip 列出已安装的包
```shell
pip list
```

## 升级pip
```shell
Python -m pip install --upgrade pip
```

## pip 指定安装源
```shell
pip install 包名 -i 镜像源

# 国内常用源:
# 阿里源：https://mirrors.aliyun.com/pypi/simple/
# 清华源：https://pypi.tuna.tsinghua.edu.cn/simple/
# 豆瓣源：http://pypi.douban.com/simple/

# 使用镜像
pip install pytest -i https://pypi.douban.com/simple
```

