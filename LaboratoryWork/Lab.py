""" 1. Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.  """

ar = [1,6,78,11,12]
#Сумма всех эл-тов >10
sum([el for el in ar if el>10])

""" 2. Пусть задан список, содержащий строки. Выведите все строки, заканчивающиеся буквой r """
string_ar = ['asdsfr', 'dsfsrwtr','fgfgd','daserwefq']
#Находим все строки, в которых последний элемент == 'r'
[el for el in string_ar if el[-1]=='r']

""" 3. Сгенерируйте и выведите cлучайную строку размером 6 символов, содержащую только цифры. Строка должна
содержать хотя бы одну цифру 3. """
from random import randint

#Счетчик кол-ва эл-тов в строке(должно быть 6)
cnt = 0
string = ''
#До 5-ого создаем элементы
while cnt<5:
    string += str(randint(0,9))
    cnt +=1
#Делаем проверку: есть ли 3 в строке, если нет - кладем ее в конец строки
if '3' in string:
    string += str(randint(0,9))
else:
    string += '3'
string

"""4. Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов"""
s = 'sdsfsaf dg fehgfhjk ekelkrgjilkreg, fdf gk,grrgrgr'
#Длина и кол-во слов, разделенных пробелами (т.к. мы расчитываем на правильное написание (, ) пунктуация также будет отделяться пробелом и нет смысла подсчитывать ее отдельно)
print(len(s))
print(len(s.split()))

"""1. Пусть дана матрица чисел размером NхN. Представьте данную матрицу в виде списка. Выведите результат сложения
всех элементов матрицы. """
#Сумма всех эл-тов диагональной матрицы
np.sum(np.diag(np.fliplr([np.arange(4)])[0], k=0))

"""2. Пусть дана матрица чисел размером NхM. Найти столбец матрицы с максимальной суммой элементов."""
#Создаем матрицу
k = np.array(
    [
        [1, 2, 5, 7],
        [3, 4, 6, 6],
        [5, 6, 34, 1]
    ]
)
#Счетчик суммы столбцов
cnt = 0
#Максимальная сумма
ma = 0
#Номер столбца
num = 0

for i in range(0,k.shape[0]):
    for st in k:
        cnt+=st[i]
    if cnt>ma:
        ma=cnt
        num = i
    cnt = 0
print(ma)
print(num+1)

"""1. Пусть список студентов представлен в виде структуры [[No, ФИО, Возраст,Группа],[No, ФИО, Возраст, Группа],[No, ФИО,
Возраст, Группа]]. Преобразуйте список в словарь вида: {No: [ФИО, Возраст, Группа], No:[....], No: [....]}"""

data = [[1, 'Name Surname Patronymic', 43,'Crossfit'],[2, 'Name Surname Patronymic', 26, 'Crossfit'],[3, 'Name Surname Patronymic',18, 'Crossfit']]
for arr in data:
    upd_data[arr[0]] = [arr[1],arr[2],arr[3]]
upd_data




"""2. Добавьте к задаче No6 для словаря возможность (без преобразования словаря обратно в список) изменить группу
студента. Поиск по «ФИО» («ФИО» студента и новый номер группы необходимо ввести с клавиатуры).

3. Добавьте к задаче No6 для словаря возможность (без преобразования словаря обратно в список) изменить возраст
студента. """
upd_data1 = {1: ['Name Surname Patronymic', 43, 'Crossfit'],2: ['Name Surnam Patronymic', 26, 'Crossfit'],3: ['Name Surname Patronymi', 18, 'Crossfit']}
print("Enter students Name Surname Patronymic:")
k = input()

search(k,upd_data1)

def search(name, data):
    print("If you want to change his group -> print: y,else print another symbol")

    a = input()
    if a == 'y':
        for arr in data:
            if data[arr][0] == name:
                print("Print new Group")
                data[arr][2] = input()
    a = 0;
    print("If you want to change his age -> print: y,else print another symbol")
    a = input()
    if a == 'y':
        for arr in data:
            if data[arr][0] == name:
                print('Print new age')
                data[arr][1] = int(input())
    return data
