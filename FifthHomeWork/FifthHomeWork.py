"""Задание 1
Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))."""
def np_reversed_array(n):
    np_array = np.arange(0,n)
    return np.fliplr([np_array])[0]
np_reversed_array(10)

"""Задание 2
Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали."""
def np_matrix_diag_count(n):
    np_array = np.diag(np.fliplr([np.arange(n)])[0], k=0)
    return np.trace(np_array)

np_matrix_diag_count(5)

'''Задание 3
Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера.
Определите какому фильму было выставлено больше всего оценок 5.0.'''

#Создаем функцию, возвращающую ключ с максимальным значением
def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

cnt = {}
#Считываем оценки из файла в словарь в виде ID_Фильма : кол-во оценок 5
with open('ratings.csv', 'r') as f:
    for line in f:
        if line.split(',')[2] == '5.0':
            cnt.setdefault(line.split(',')[1], 0)
            cnt[line.split(',')[1]] += 1



film = {}
#Считываем фильмы в словарь в виде ID_Фильма : "Название фильма"
with open('movies.csv', 'r') as f:
    for line in f:
        film.setdefault(line.split(',')[0], 0)
        film[line.split(',')[0]] = line.split(',')[1]

#Выводим название фильма с максимальным кол-вом оценок 5
print(film[keywithmaxval(cnt)])


'''Задание 4
По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года.
Не учитывайте в расчетах отрицательные значения quantity.'''
import pandas as pd
data = pd.read_csv('power.csv')
data[((data['country'] == 'Estonia') | (data['country'] == 'Lithuania') | (data['country'] == 'Latvia')) & ((data['category'] == 4) |(data['category'] == 12) | (data['category'] == 21)) & (data['year'] >= 2005) & (data['year'] <= 2010) & (data['quantity']>=0)]

'''Задание 5
Решите систему уравнений:
4x + 2y + z = 4
x + 3y = 12
5y + 4z = -3'''
from numpy import linalg

a = np.array( [ [4, 2, 1], [1, 3, 0], [0, 5, 4] ] )
b = np.array( [4, 12, -3] )

linalg.solve(a, b)
