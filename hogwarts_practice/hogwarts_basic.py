# list_hogwarts=[1,2,3]
# list_hogwarts.append(0)
# list_hogwarts.insert(1,4)
# list_hogwarts.remove(1)
# y=list_hogwarts.pop(1)
# list_hogwarts.sort(reverse=False)
# list_hogwarts.reverse()
# print(list_hogwarts)
# print(y)


# list_square=[]
# for i in range(1,4):
#     list_square.append(i**2)
# print(list_square)
# list_square=[i**2 for i in range(1,4)]
# print(list_square)
# list_square=[i**2 for i in range (1,4) if i !=1]
# print(list_square)
# list_square=[i*j for i in range(1,4) for j in range(1,4)]
# print(list_square)
# list_square=[]
# for i in range(1,4):
#     for j in range(1,4):
#         list_square.append(i*j)
# print(list_square)


# tuple_hogwarts=(1,2,3)
# tuple_hogwarts2=1,2,3
# print("tuple_hogwarts",tuple_hogwarts)
# print(type(tuple_hogwarts))
# print("tuple_hogwarts2",tuple_hogwarts2)
# print(type(tuple_hogwarts2))
# tuple_hogwarts=[1,2,3]
# tuple_hogwarts[0]="a"
# print(tuple_hogwarts)
# a=[1,2,3,"a","a"]
# tuple_hogwarts=(1,2,a)
# print(id(tuple_hogwarts))
# tuple_hogwarts[2][1]="a"
# print(id(tuple_hogwarts))
# print(a.count("a"))
# print(a.index(1))
""""
集合
"""
# a={1,2,3,4}
# b={1,3,4,5}
# # print(a.union(b))
# # print(a.intersection(b))
# # print(a.difference(b))
# print ( {i for i in "adjfldjfslfjdslfjdslfslfa"})
"""
字典
"""
# hogwarts_dict={"a":1,"b":2}
# hogwarts_dict2=dict(a=1,b=2)
# print(hogwarts_dict)
# print(type(hogwarts_dict))
# print(hogwarts_dict2)
# print(type(hogwarts_dict2))

# a={"a":1,"b":2}
# b=dict(a=1,b=2)
# # print(a.keys())
# # print(a.values())
# # print(a.pop("a"))
# # print(a)
# # 返回被删除的键值对
# print(a.popitem())
# # 删除掉上面执行的键值对后，还剩的元素
# print(a)


#
# a={}
# b=a.fromkeys([1,3,4],"a")
# print(b)


# print({i: i * 2 for i in range(1, 5)})









