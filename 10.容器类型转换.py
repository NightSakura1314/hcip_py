# list列表
# tuple元组
# set集合
# dict 字典

n = '123'
res = list(n)
print(n, type(n), res, type(res))
# 结果 123 <class 'str'> ['1', '2', '3'] <class 'list'>

# 字符串转换为列表时，会把字符串中的每一个字符当成列表的元素
# 数字类型是非容器类型，不能转换为列表
# 集合，元组可以转换为list列表类型
# 字典可以转换为list列表类型，只保留字典的键

n = '123'
res = tuple(n)
print(n, type(n), res, type(res))
# 结果 123 <class 'str'> ('1', '2', '3') <class 'tuple'>
# 数字类型 非容器类型不能转换为元组
# 其他容器类型的数据进行转换时，和列表一样

a = [[1, 2], ['a', 'b']]
res = dict(a)
print(res, type(res))
# 结果：{1: 2, 'a': 'b'} <class 'dict'>
# 数字类型 非容器类型，不能转换为字典
# 字符串不能直接转换为字典
# 列表可以转换为字典，要求是一个二级列表，并且每个二级元素只能有一个值
# 二级元组也可以转换为字典