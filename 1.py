import math

import numpy as np

list3 = [1, 2]
scores_l = [[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
         [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
         [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
         [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
         [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
         [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
         [6, 0, 65, 78, 43, 22, 38, 88, 94, 100],
         [77, 28, 39, 41, 0, 81, 45, 54, 98, 12],
         [66, 0, 88, 0, 44, 0, 55, 100, 12, 11],
         [17, 70, 86, 96, 56, 23, 32, 49, 70, 80],
         [20, 24, 76, 50, 29, 40, 3, 2, 5, 11],
         [33, 63, 28, 40, 51, 100, 98, 87, 22, 30],
         [16, 54, 78, 12, 25, 35, 10, 19, 67, 0],
         [100, 88, 24, 33, 47, 56, 62, 34, 77, 53],
         [50, 89, 70, 72, 56, 29, 15, 20, 0, 0]]
scores = np.array(scores_l)
# list1 = [[1, 2, 3],
#          [4, 5, 6]]
# print(list1, type(list1))
# a = np.array(list1)
# print(a, type(a))
list2 = [[1, 2.5, 3],
         [4, 'shgfsdj', scores_l]]
# print(list2, type(list2))
b = np.array(list2, dtype=object)
print(scores)
print(b, type(b))
print('-----------------')
print('1. Основные свойства массивов numpy')
print('Размерность массива: ', b.ndim)
print('Размер массива: ', b.size)
print('Форма массива: ', b.shape)
print('Тип данных массива: ', b.dtype)
print('-----------------')
print('2. Создание массивов numpy')
# a = np.zeros([2, 3, 2])
# print(a)
# a = np.ones([2, 3, 2], dtype=np.int32)
# print(a)
# a = np.full([2, 3], 8)
# print(a)
# a = np.full_like(scores, 3)
# print(a)
# a = np.eye(6, dtype=np.int32)
# print(a)
# a = np.random.rand(6, 6)*6-3
# print(a)
# a = np.random.randint(6, 13, [6, 6])
# print(a)
print('-----------------')
print('3. Slice/нарезка массивов numpy')
# print(scores)
# print(scores[-1])
# print(scores[-1][1])
# print(scores[-1, 1])
# scores = np.array([[[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
#          [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
#          [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
#          [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
#          [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
#          [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
#          [6, 0, 65, 78, 43, 22, 38, 88, 94, 100],
#          [77, 28, 39, 41, 0, 81, 45, 54, 98, 12],
#          [66, 0, 88, 0, 44, 0, 55, 100, 12, 11],
#          [17, 70, 86, 96, 56, 23, 32, 49, 70, 80],
#          [20, 24, 76, 50, 29, 40, 3, 2, 5, 11],
#          [33, 63, 28, 40, 51, 100, 98, 87, 22, 30],
#          [16, 54, 78, 12, 25, 35, 10, 19, 67, 0],
#          [100, 88, 24, 33, 47, 56, 62, 34, 77, 53],
#          [50, 89, 70, 72, 56, 29, 15, 20, 0, 0]]])
# print(scores)
# print(scores[0][-1])
# print(scores[0][-1][1])
# print(scores[0, -1, 1])
# print(scores[:, 2:-1, 4])
# print(scores[0, 2:-1, 4])
# scores[0, 2:-1, 4] = 0
# print(scores)
print('-----------------')
print('4. Операторы массивов numpy')
# a = np.full_like(scores[0], 4)
# b = np.full_like(scores[0], 3)
# c = a + b
# print(a)
# print(b)
# print(c)
# c = a - b
# print(c)
# c = a * b
# print(c)
# print(scores[0].shape)
# b = b.T
# print(a.shape)
# print(b.shape)
# c = a @ b
# print(c)
# b = b.T
# c = a / b
# print(c)
# c = a + b * 2
# print(c)
# c = np.power(a, 2)
# print(c)
print('-----------------')
print('5. Стандартные функции массивов numpy')
# print(scores)
# print(scores.min(axis=0))
# print(scores.min(axis=1))
# print(scores.max(axis=0))
# print(scores.argmax(axis=0))
# help(np.argmax)
# # a = np.array([[1, 2], [3, 4]], dtype=np.int32)
# a = np.full_like(scores, 3, dtype=np.int32)
# print(a)
# # print(np.sin(a))
# # print(np.exp(a))
# print(np.prod(a))
print('---------------')
print('6. Массивы numpy с множеством измерений')
cube1 = np.random.randint(1,3,[3,3,3])
cube2 = np.random.randint(3,5,[3,3,3])
cube3 = np.random.randint(5,7,[3,3,3])
arr4 = np.array([cube1, cube2, cube3])
# print(arr4)
arr5 = np.array([arr4, arr4, arr4])
print(arr5)
print(arr5.shape)
print(arr5[1, -1, :, :, -1])
print(arr5[1, -1, ..., -1])
# print('---------------')
# print('7. Булевы массивы Numpy')
# a = np.random.rand(3,4) * 5
# b = np.random.rand(3,4) * 5
# c = a>2
# print(a)
# print(c)
# print(a[a>2])
# print(b)




