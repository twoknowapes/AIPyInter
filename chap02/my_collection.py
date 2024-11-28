class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)


# 创建一个自定义集合对象
my_collection = MyCollection([1, 2, 3, 4])

# 使用内置方法和魔术方法
print(f"集合的长度: {len(my_collection)}")
print(f"第一个元素: {my_collection[0]}")
my_collection[1] = 5
print(f"修改后的集合: {my_collection.items}")
del my_collection[2]
print(f"删除元素后的集合: {my_collection.items}")

# 迭代集合
for item in my_collection:
    print(item)
