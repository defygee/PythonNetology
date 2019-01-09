
#Задание 1
"""
Используем файл keywords.csv.

Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определенному региону.
 Т. е. если поисковый запрос содержит название города региона, то в столбце 'region' пишется название этого региона.
  Если поисковый запрос не содержит названия города, то ставим 'undefined'.

Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

geo_data = {

    'Центр': ['москва', 'тула', 'ярославль'],

    'Северо-Запад': ['петербург', 'псков', 'мурманск'],

    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

}

Результат классификации запишите в отдельный столбец region.
"""

def check(x):
    geo_data = {

        'Центр': ['москва', 'тула', 'ярославль'],

        'Северо-Запад': ['петербург', 'псков', 'мурманск'],

        'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

    }
    for region in geo_data:
        if x in geo_data[region]:
            return region
    return 'undefined'

l = pd.read_csv('keywords.csv')
l['region'] = l['keyword'].apply(lambda x: check(x))


def rating(x):
    if x<=2:
        return 'low'
    if x<=4:
        return 'med'
    else:
        return 'high'

k = pd.read_csv('ratings.csv')
k.columns = ['userid','movieid','rating','timestamp']
k['class'] = k['rating'].apply(lambda x: rating(x))









k = pd.read_csv('movies.csv')

def finder(x):
    for el in arr:
        if str(el) in x:
            return el
    return 1900


k['production_year'] = k['title'].apply(lambda x: finder(x))
k['year'] = k['title'].apply(lambda x: finder(x))
