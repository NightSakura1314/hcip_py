#集合的定义方式
vars={1,2,3,'a','b'}
print(vars,type(vars))
#输出 {'b', 2, 3, 1, 'a'} <class 'set'>
vars=set('123456')
print(vars,type(vars))
#输出 {'3', '4', '2', '6', '1', '5'} <class 'set'>
vars=set()
print(vars,type(vars))
#输出 set() <class 'set'>
#无法获取集合中的单个元素，但是可以添加和删除元素
a= {1,2,3,'a','b'}
a.add('c')
print(a)
#输出 {1, 2, 3, 'a', 'b', 'c'}
a.discard('a')
print(a)
#输出  {1, 2, 3, 'c', 'b'}

#检查当前元素是否在集合中
print(1 in a)
print('d' in a)
#输出 True  False

#集合主要用于运算，交集，差集，并集，对称集合
a = {1,2,3,'a','b'}
b = {1,'a',22,33}
print(a & b) #交集 {1, 'a'}
print(a - b) #差集 {2, 3, 'b'} a集合有，b集合没有
print(a | b) #并集 {1, 2, 3, 33, 'a', 22, 'b'}
print( a ^ b) #对称差集 {33, 2, 3, 22, 'b'} 得出都没有的集合


