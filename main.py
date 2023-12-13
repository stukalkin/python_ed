n = 5
factN = 1
while n > 1:
    factN = factN * (n)
    n = n - 1
print (factN)


A = int(input("Введите число: "))

f1 = 0
f2 = 1
f3 = 1
i = 2
while f3 <= A:
    i = i + 1
    f3 = f2 + f1
    if f3 == A:
        print(f"{A} - {i} - ое число Фибоначчи")
        break
    f1 = f2
    f2 = f3
    print(f3)
else:
    print(-1)




num = int(input('Введите число: '))

if num <= 1:
    print(-1)
else:
    fib_curr, fib_next = 0, 1
    n = 2
    while fib_next <= num:
        if fib_next == num:
            print(n)
            break
        fib_curr, fib_next = fib_next, fib_curr + fib_next
        n += 1
    else:
        print(-1)






numbers = "-20 30 -40 50 10 -10".split(" ")

length = 0
max_length = 0

for num in numbers:
    if int(num) > 0:
        length += 1
    else:
        length = 0
    
    if length > max_length:
        max_length = length

print(max_length)






# Задача №13. Решение в группах Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50 
# Input:    6 -> -20 30 -40 50 10 -10 
# Output: 2

# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите температуру: "))
#     if temp >= 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

# import random
# array = [random.randint(-50,50) for i in range(6)]
# temp_count = 0
# count = 0
# print(array)
# for temp in array:
#     if temp>0:
#         temp_count+=1
#     else:
#         count = max(count,temp_count)
#         temp_count = 0
# count = max(count,temp_count)
# print(count)

# length = 0  
# max_length = 0  

# for i in range(n):
#     el = int(numbers[i])

#     if el > 0:
#         length += 1
#     else:
#         length = 0

#     if length > max_length:
#         max_length = length


# print(max_length)


# import random
# import os

# os.system("cls")

# N = int(input("Введите число N рассматриваемых дней (1 ≤ N ≤ 100): "))
# summ = 0
# count = 0
# # listtemp = [-36, -45, -25, 11, 49, 49]
# for i in range(N):
#     t = random.randint (-50, 50)
#     if t > 0:
#         count+=1
#     else: 
#         if count > summ:
#             summ = count
#         count=0
#     print(t, end=' ')
# print()
# if count > summ:
#     summ = count
# print("Наибольшее кол-во дней оттепели равно ", summ)

# l = [1, 2, 3, 4, 5]
# for i in range(len(l)):
#     print(i)




import random
count = 0
result = 0
n = int(input("Введите колличество дней: "))
for i in range(n):
    i = random.randint(-50, 50)
    if i > 0:
        count += 1
        result += count
    elif i < 0:
        if result <= count:
            count = 0
        else:
            result = count   
print(f" Самая длинная оттепель длилась - {result}")






from random import randint

num_watermelons = int(input('Введите кол-во арбузов: '))
watermelons_weight = list(map(int, input('Введите массу арбуза: ').split()))
# watermelons_weight = [randint(1, 10) for _ in range(num_watermelons)]
# можно сделать генератор списка случайных чисел, для масс арбузов.

if watermelons_weight:
    min_weight = max_weight = watermelons_weight[0]

    for i in range(1, num_watermelons):
        if watermelons_weight[i] < min_weight:
            min_weight = watermelons_weight[i]
        elif watermelons_weight[i] > max_weight:
            max_weight = watermelons_weight[i]

    print(f'Для тёщи: {min_weight} кг.\nДля себя: {max_weight} кг.')
else:
    print('Список масс арбузов пуст!')




#Задача №17. Решение в группах
#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6


list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
dim_1 = set(list_1)
print(len(dim_1))
print(len(set([1, 1, 2, 0, -1, 3, 4, 4])))





#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
print(list_1)
k = 3
#temp = None
for _ in range(k):
    temp = list_1[-1]
    for i in range(len(list_1) - 1):
        list_1[len(list_1) - i - 1] = list_1[len(list_1) - i - 2]
    list_1[0] = temp
print(list_1)






#Семинар 3. Списки и словари
#Задача №21. Решение в группах
#Напишите программу для печати всех уникальных
#значений в словаре.
#Input: lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#           {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}



lst_obj = [{"V": "S001", "h": "S008"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]
my_set = set()

# традиционный итератор с функцией add() для множества
for el in lst_obj:
    for item in el.values():
        my_set.add(item)

print(my_set)
# множественное включение set comrehension
my_set = set(item for el in lst_obj for item in el.values())

print(my_set)






#Задача №23. Решение в группах
#Дан массив, состоящий из целых чисел. Напишите
#программу, которая подсчитает количество
#элементов массива, больших предыдущего (элемента
#с предыдущим номером)
#Input: [0, -1, 5, 2, 3]
#Output: 2 (-1 < 5, 2 < 3)



list_nums = [0, -1, 5, 2, 3]
count = 0

for i in range(1, len(list_nums)):
    if list_nums[i] > list_nums[i - 1]:
        count += 1
print(count)



#Задача №25. Решение в группах
#Напишите программу, которая принимает на вход
#строку, и отслеживает, сколько раз каждый символ
#уже встречался. Количество повторов добавляется к
#символам с помощью постфикса формата _n.
#Input: a a a b c a a d c d d
#Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


lst = "a a a b c a a d c d d".split()
print(lst)
dct = {}
for item in lst:
    if item in dct:
        print(f"{item}_{dct[item]}", end=' ')
    else:
        print(item, end=' ')
    dct[item] = dct.get(item, 0) + 1




    
#Задача №27. Решение в группах
#Пользователь вводит текст(строка). Словом считается
#последовательность непробельных символов идущих
#подряд, слова разделены одним или большим числом
#пробелов. Определите, сколько различных слов
#содержится в этом тексте.
#Input: She sells sea shells on the sea shore The shells
#that she sells are sea shells I'm sure.So if she sells sea
#shells on the sea shore I'm sure that the shells are sea
#shore shells




input_string_list = input_string.split()
input_string_set = set(input_string_list)

print(len(input_string_set))



#Решение в группах
#Ваня и Петя поспорили, кто быстрее решит
#следующую задачу: “Задана последовательность
#неотрицательных целых чисел. Требуется определить
#значение наибольшего элемента
#последовательности, которая завершается первым
#встретившимся нулем (число 0 не входит в
#последовательность)”. Однако 2 друга оказались не
#такими смышлеными. Никто из ребят не смог до
#конца сделать это задание. Они решили так: у кого
#будет меньше ошибок в коде, тот и выиграл спор. За
#помощью товарищи обратились к Вам, студентам.


n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(f"Максимальное число: {max_number}")

#Петя:
n = int(input())
max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(f"Максимальное число: {max_number}")



#Задача №31. Решение в группах
#Последовательностью Фибоначчи называется
#последовательность чисел a0
#, a1
#, ..., an
#, ..., где
#a0 = 0, a1 = 1,
#ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
#Input: 7
#Output: 21


def fibonacci(n):
    if n < 3:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n = 7
print(fibonacci(n))

fib1, fib2 = 0, 1
for i in range(0, n):
    fib1, fib2 = fib2, fib2 + fib1
print(fib2)


#Задача №33. Решение в группах
#Хакер Василий получил доступ к классному журналу и
#хочет заменить все свои минимальные оценки на
#максимальные. Напишите программу, которая
#заменяет оценки Василия, но наоборот: все
#максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1


def min_to_max(grade_list, count, x):
    if count < 0:
        return grade_list
    count -= 1
    if grade_list[count] == x:
        grade_list[count] = min(grade_list)
    return min_to_max(grade_list, count, x)


list_1 = [1, 3, 3, 3, 4]
cnt = 5

print(min_to_max(list_1, cnt, max(list_1)))


#Задача №35. Решение в группах
#Напишите функцию, которая принимает одно число и
#проверяет, является ли оно простым
#Напоминание: Простое число - это число, которое
#имеет 2 делителя: 1 и n(само число)
#Input: 5
#Output: yes

def func_1(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag

print(func_1(10))


def func_2(num, flag=True, i=2):
    if i < int(num ** 0.5) + 1:
        if num % i == 0:
            flag = False
        return func_2(num, flag, i+1)
    return flag
print(func_2(31))


#Задача №37. Решение в группах
#15 минут
#Дано натуральное число N и
#последовательность из N элементов.
#Требуется вывести эту последовательность в
#обратном порядке.
#Примечание. В программе запрещается
#объявлять массивы и использовать циклы
#(даже для ввода и вывода).
#Input: 2 -> 3 4
#Output: 4 3


def rev(new):
    if len(new) == 1:
        return new
    return new[-1] + rev(new[:-1])


orig = '1 2 3 4 5 6 7'
x = 5
print(rev(orig))


def rev(n):
    if n > 0:
        num = int(input("Введите число: "))
        rev(n - 1)
        print(num, end=' ')


rev(2)


"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv

data = read_csv('california_housing_test.csv')
print(type(data))
print(data.shape)
print(data.dtypes)
print(data.info())
print(data.describe())




'''
Задача №59. Решение в группах
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
'''

from pandas import read_csv
data = read_csv('california_housing_test.csv')
# # 1. Проверить есть ли в файле пустые значения
# print(data.isnull().sum())
# # 2. Показать median_house_value где median_income < 2
# res = data[data['median_income'] < 2]['median_house_value']
# print(res)
# 3. Показать данные в первых 2 столбцах
# res = data[['longitude', 'latitude']]
# print(res)
# res = data.iloc[:, :2]          #получение 2-х стлбцов через срезы, 1: - все строки; 2: - только первые 2 слобца
# print(res)
# 4. Выбрать данные где housing_median_age < 20 и  median_house_value > 70000
res = data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70_000)]
print(res)



'''
Задача №61. Решение в группах
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
'''

from pandas import read_csv
data = read_csv('california_housing_test.csv')

# 1. Определить какое максимальное и минимальное значение median_house_value
# print(f"{data['median_house_value'].max()}, {data['median_house_value'].min()}")

# # 2. Показать максимальное median_house_value, где median_income = 3.1250
# print(data[data['median_income'] == 3.1250]['median_house_value'].max())

# # 3. Узнать какая максимальная population в зоне минимального значения median_house_value
res = data[data['median_house_value'] == data['median_house_value'].min()]['population'].max()
print(res)

