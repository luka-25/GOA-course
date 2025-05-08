lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

lst.append("hello")
print(lst)  # [1, 2, 3, 4, 'hello']



lst = [1, 2, 3]
lst.clear()
print(lst)  # []

lst = ["a", "b"]
lst.clear()
print(lst)  # []



lst = [1, 2, 2, 3]
print(lst.count(2))  # 2

lst = ['a', 'b', 'a']
print(lst.count('a'))  # 2



lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]

lst.extend("xy")
print(lst)  # [1, 2, 3, 4, 'x', 'y']



lst = [5, 3, 7, 3]
print(lst.index(3))  # 1

lst = ['a', 'b', 'c']
print(lst.index('c'))  # 2



lst = [1, 2, 3]
lst.insert(1, 10)
print(lst)  # [1, 10, 2, 3]

lst.insert(0, "start")
print(lst)  # ['start', 1, 10, 2, 3]



lst = [1, 2, 3]
print(lst.pop())   # 3
print(lst)         # [1, 2]

print(lst.pop(0))  # 1
print(lst)         # [2]



lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)  # [1, 3, 2]

lst.remove(3)
print(lst)  # [1, 2]



lst = [5, 2, 9, 1]
lst.sort()
print(lst)  # [1, 2, 5, 9]

words = ["banana", "apple", "cherry"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry']
