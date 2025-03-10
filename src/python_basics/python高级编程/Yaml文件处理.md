# YAML文件处理
## 简介
>YAML 全称其实是 YAML Ain't a Markup Language（YAML不是一种标记语言）的递归缩写，所以它强调的是数据本身，而不是以标记为重点。

>YAML 是一种可读性非常高，与程序语言数据结构非常接近。同时具备丰富的表达能力和可扩展性，并且易于使用的数据标记语言。

## 为什么要使用 YAML 文件
其实 YAML 文件也是一种配置文件，但是相较于 ini，conf 配置文件来说，更加的简洁，操作简单，还能存放不同类型的数据，
而像 ini 存储的值就都是字符串类型，读取之后还要手动转换。

## YAML的基本语法规则
* 大小写敏感
* 使用缩进表示层级关系
* 缩进时不允许使用 Tab 键，只允许使用空格。（可以将你的 IDE 的 tab 按键输出替换成 4 个空格）
* 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
* #表示注释

## YAML 的数据结构
* 对象：键值对的集合，又称为映射 mapping / 哈希 hashes / 字典 dictionary
* 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
* 纯量 scalars：单个的、不可再分的值

### 对象类型
对象的一组键值对，使用冒号结构表示，会转换成 Python 中的字典。
```yaml
# yaml格式
animals: dog
```

```python
# python格式
{'animals': 'dog'}
```

```yaml
# yaml格式
person: {name: Tom, age: 20, gender: male}
```

```python
# python格式
{
    'person': {
         'name': 'Tom',
         'age': 20,
         'gender': 'male'
    }
}
```

### 数组类型
数组类型使用 - 为前缀，每个元素独占一行，通过缩进关系表示层级包含关系，会转换成 Python 中的列表。
```yaml
# yaml格式
- one
- two
- three
- four
- five
```

```python
# python格式
['one', 'two', 'three', 'four', 'five']
```

```yaml
# yaml格式
- 
    - 1
    - 2
    - 3
-
    - 4
    - 5
    - 6
```

```python
# python格式
[[1, 2, 3], [4, 5, 6]]
```

### 纯量类型
>纯量类型是最基本的、不可再分的值；类似基本数据类型。

* 字符串: 不需要使用双引号包裹
* 布尔值: true、True、false、False都可以
* 整数
* 浮点数
* 时间，时间使用 ISO 8601 格式，时间和日期之间使用T连接，最后使用+代表时区
* 日期，日期必须使用 ISO 8601 格式，即 yyyy-MM-dd
* Null: ~ 表示 Null

```yaml
# yaml格式
int: 12
float: 12.3
string: pets
bool: true
None: null
time: 2001-12-14t21:59:43.10-05:00
date: 2018-03-21
```

```python
# python格式
{
   'int': 12, 
   'float': 12.3, 
   'string': 'pets', 
   'bool': True, 
   'None': None, 
   'time': datetime.datetime(2001, 12, 14, 21, 59, 43, 100000, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=68400))), 
   'date': datetime.date(2018, 3, 21)
}
```

### 复杂结构
```yaml
# yaml格式
cool_list:
  - 10
  - 15
  - 12

hard_list:
  - {key: value}
  - [1,2,3]
  - test:
      - 1
      - 2
      - 3

twice_list:
  -
    - {a: AA}
    - {b: BB}
    - {c: CC}
```

```python
# python格式
{
    'cool_list': [10, 15, 12],
    'hard_list': [
        {'key': 'value'},
        [1, 2, 3],
        {
            'test': [1, 2, 3]
        }
    ],
    'twice_list': [
        [
            {'a': 'AA'}, 
            {'b': 'BB'},
            {'c': 'CC'}
        ]
    ]
}
```

>Tips：有 : 后面的内容就解析成字典，有 - 后面的内容就解析成列表的元素