# # li = [10, 2, 3, 4, 7, 11, 33]

# # # newli = []

# # # for i in li:
# # #     if i % 2 != 0:
# # #         newli.append(i)
# # newli = [i for i in li if i % 2 != 0]


# # print(newli)

# li = [1, 3, 2, 4, 7, 11]

# newli = []

# # for i in li:
# #     if i % 2 != 0:
# #         newli.append(i + 10)
# newli = [i + 10 for i in li if i % 2 != 0]

# print(newli)

li = [7, 9, 11, 2, 4, 19, 10, 20]

# for i in li:
#     if i % 2 != 0:
#         print(i, 'odd')
#     else:
#         print(i, 'even')

newli = ["even" if i % 2 == 0 else "odd" for i in li]

print(newli)