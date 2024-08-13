'''
[expression for item in iterable if condition]
expression 是新列表中每个元素的表达式。
item 是从 iterable 中迭代出来的元素。
iterable 是一个可迭代对象，例如列表、元组或集合。
condition 是一个可选的条件表达式，用于过滤元素。
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened) 