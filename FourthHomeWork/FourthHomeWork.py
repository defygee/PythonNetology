from datetime import datetime
from datetime import timedelta


def data_diff(start_date, end_date):

    date_start = datetime.strptime(start_date,'%Y-%m-%d')
    date_end = datetime.strptime(end_date,'%Y-%m-%d')
    current = start_date

    while current <= date_end:
        print(current.strftime('%Y-%m-%d'))

        current += timedelta(days=1)
    return current




from datetime import datetime
from datetime import timedelta
import traceback

def data_diff(start_date, end_date):

    try:
        date_start = datetime.strptime(start_date,'%Y-%m-%d')
        date_end = datetime.strptime(end_date,'%Y-%m-%d')
    except Exception:
        print(traceback.print_exc())
        return []
    current = date_start

    while current <= date_end:
        print(current.strftime('%Y-%m-%d'))

        current += timedelta(days=1)
    return current



    def data_check(date):

    try:
        date_date = datetime.strptime(date,'%Y-%m-%d')
    except:
        return False
    return True


import datetime
from datetime import datetime, date, time
from datetime import timedelta
import calendar

def date_arr():

    now = datetime.now()

    if now.day == 1:
        first = datetime(now.year,now.month-1,1)
        end = datetime(calendar.monthrange(now.year, now.month-1, calendar.monthrange(now.year,now.month-1)[1])
        while first < end:
            print(first.strftime("%Y-%m-%d"))
            first = datetime(now.year,now.month,first.day+1)

    now -= timedelta(days = 1)
    first = datetime(now.year,now.month,1)
    while first < now:
        print(first.strftime("%Y-%m-%d"))
        first = datetime(now.year,now.month,first.day+1)



    import calendar
def day(time):
    now = datetime.now()
    if time == 'today':
        return now.strftime("%Y-%m-%d")
    if time == 'last monday':
        return (now - timedelta(days=datetime.today().weekday()+7)).strftime("%Y-%m-%d")
    if time == 'last day':
        return calendar.monthrange(now.year,now.month)[1]
    else:
        return 'Ошибка'


import datetime
from datetime import datetime, date, time
from datetime import timedelta
import calendar


def weeks(start_date,end_date):
    date_start = datetime.strptime(start_date,'%Y-%m-%d')
    date_end = datetime.strptime(end_date,'%Y-%m-%d')
    week_count = 0
    while date_end.day - date_start.day >= 7:
        week_count += 1
        print("{} week: {} - {}".format(week_count, date_start.strftime("%Y-%m-%d"),(date_start + timedelta(days=7)).strftime("%Y-%m-%d")))
        date_start = date_start + timedelta(days=7)

weeks('2018-02-02','2018-02-16')
