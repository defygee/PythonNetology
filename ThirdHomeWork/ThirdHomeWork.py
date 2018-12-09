#Задание 1
"""Дан список вида:
data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
]

Напишите функцию, которая возвращает сумму элементов на диагонали. Т. е. 13+32+23+35.
"""

data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
]


def data_cross_plus(data):
    #Создаем переменную для подсчета значений
    count = 0
    #Складываем значения по диагонали(data[0][0]+data[1][1] ... + data[i][i])
    for i in range(len(data)):
        count+=data[i][i]
    return count
#Вывод значения
print(data_cross_plus(data))
"""
Вывод:
103
"""
########################################################################################################################################################################
#Задание 2
"""
Дан список чисел, часть из которых имеют строковый тип или содержат буквы.
Напишите функцию, которая возвращает сумму квадратов элементов, которые могут быть числами.
data = [1, '5', 'abc', 20, '2']
"""


#Функция, которая проверяет значение s(является ли оно целочисленным)
#Строки с целыми числами также считаются целым целочисленными значениеми
def isint(s):
    #Пробуем, появится ли ошибка типа, если нет - возвращаем True
    try:
        int(s)
        return True
    #Еслм же ошибка есть - False
    except ValueError:
        return False


#Создадим функцию, в которой складываются квадраты всех целочисленных значений в списке data
#строки с целочисленными значениями также считаются
def square_count(data):
    count = 0
    for i in data:
        if isint(i):
            count += int(i)**2
    return count

data = [1, '5', 'abc', 20, '2']

#Вывод суммы квадратов
print(square_count(data))
"""
Вывод:
430
"""


#Задание 3
"""
Напишите функцию, которая возвращает название валюты (поле 'Name') с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js
"""
import requests

def max_val():
    #Записываааем данные из https://www.cbr-xml-daily.ru/daily_json.js в переменную r
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    #Записываем данные из словаря 'Valute' в переменную val
    val = r.json()['Valute']

    #Создаем переменные названия для записи максимального значения value и названия этой валюты

    name = ''
    max_val = 0

    for dicts in val:
        #Находим максимальное значение валюты и записываем ценность и название в переменные
        if val[dicts]['Value']>max_val:
            max_val = val[dicts]['Value']
            name = val[dicts]['Name']
    #Функция возвращает имя валюты с максимальным значением Value
    return name

print(max_val())
"""
Вывод:
Китайских юаней
"""

#Задание 4
"""
Последнее упражнение с занятия
1. Добавьте в класс еще один формат, который возвращает название валюты (например, 'Евро').

2. Добавьте в класс параметр diff (со значениями True или False), который в случае значения True в методах eur и usd будет возвращать не курс валюты, а изменение по сравнению в прошлым значением.
"""

class Rate():



    def __init__(self, format='value'):
        self.format = format

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

        return 'Error'
    #Функция eur, при diff в значении True - выводит разность курсов, при False - значение Value
    def eur(self,diff):
        """Возвращает курс евро на сегодня в формате self.format"""
        response = self.exchange_rates()
        if (diff == False):
            return self.make_format('EUR')
        if (diff == True):
            return abs(self.make_format('EUR') - response['EUR']['Previous'])
    #Функция usd, при diff в значении True - выводит разность курсов, при False - значение Value
    def usd(self,diff):
        """Возвращает курс доллара на сегодня в формате self.format"""
        response = self.exchange_rates()
        if (diff == False):
            return self.make_format('USD')
        if (diff == True):
            return abs(self.make_format('USD') - response['USD']['Previous'])

    #Функция, возвращающая имя по charcode
    def name(self, charcode):

        response = self.exchange_rates()

        if charcode in response:
            return response[charcode]['Name']

#Вывод разности курсов euro
a = Rate()
a.eur(True)

#Задание 5
"""
Напишите функцию, возвращающую сумму первых n чисел Фибоначчи
"""

#Рекурсионная функция Fib выводит значение числа Фибоначчи с индексом n
def Fib(n):
    if n >= 2:
        return Fib(n-1) + Fib(n-2)
    if n == 1:
        return 1
    if n == 0:
        return 0

#Функция суммы чисел Фибоначчи до числа с индексом n(включительно)
def sum_fib(n):
    #Присваиваем k зн-е n
    k=n
    #Переменная суммы
    summary = 0
    #Складываем значения всех чисел Фибоначчи, пока k!=0(С каждым проходом вычитаем из k 1)
    while(k!=0):
        summary+=Fib(k)
        k-=1
    return(summary)

#Вывод суммы первых пяти чисел
sum_fib(5)
"""
Вывод:
12
(1+1+2+3+5=12)
"""

#Задание 6
"""
Напишите функцию, преобразующую произвольный список вида ['2018-01-01', 'yandex', 'cpc', 100] в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
"""

a = ['2018-01-01', 'yandex', 'cpc', 100]
#Функция, возвращающая словарь в формате {'2018-01-01': {'yandex': {'cpc': 100}}} от списка вида ['2018-01-01', 'yandex', 'cpc', 100]
def new_arr(a):
    return {a[0]:{a[1]:{a[2]:a[3]}}}

new_arr(a)
"""
Вывод:
{'2018-01-01': {'yandex': {'cpc': 100}}}
"""
