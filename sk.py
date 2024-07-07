import datetime

def date_create():
    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now() + delta_1
    if int(now.day) < 10:
        day_edit = '0' + str(now.day)
    else:
        day_edit = now.day

    if int(now.month) < 10:
        month_edit = '0' + str(now.month)
    else:
        month_edit = now.month

    res = f'{day_edit}.{month_edit}.{now.year}'

    return res
def date_tomorrow_create():
    delta_1 = datetime.timedelta(days=1)
    now = datetime.datetime.now() + delta_1

    if int(now.day) < 10:
        day_edit = '0' + str(now.day)
    else:
        day_edit = now.day

    if int(now.month) < 10:
        month_edit = '0' + str(now.month)
    else:
        month_edit = now.month

    res = f'{day_edit}.{month_edit}.{now.year}'

    return res
def date_yes_create():
    delta_1 = datetime.timedelta(days=1)
    now = datetime.datetime.now() - delta_1

    if int(now.day) < 10:
        day_edit = '0' + str(now.day)
    else:
        day_edit = now.day

    if int(now.month) < 10:
        month_edit = '0' + str(now.month)
    else:
        month_edit = now.month

    res = f'{day_edit}.{month_edit}.{now.year}'

    return res
def date_and_time_create():
    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now() + delta_1
    if int(now.day) < 10:
        day_edit = '0' + str(now.day)
    else:
        day_edit = now.day

    if int(now.month) < 10:
        month_edit = '0' + str(now.month)
    else:
        month_edit = now.month

    if int(now.hour) < 10:
        hour_edit = '0' + str(now.hour)
    else:
        hour_edit = now.hour

    if int(now.minute) < 10:
        minute_edit = '0' + str(now.minute)
    else:
        minute_edit = now.minute

    res = f'{hour_edit}:{minute_edit} - {day_edit}.{month_edit}.{now.year}'

    return res
def time_create():
    delta_1 = datetime.timedelta(hours=5)
    now = datetime.datetime.now()


    if int(now.hour) < 10:
        hour_edit = '0' + str(now.hour)
    else:
        hour_edit = now.hour

    if int(now.minute) < 10:
        minute_edit = '0' + str(now.minute)
    else:
        minute_edit = now.minute

    res = f'{hour_edit}:{minute_edit}'

    return res