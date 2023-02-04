from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    BIRTHDAY_WEEK = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }

    WEEKEND = ('Saturday', 'Sunday')

    current_date = date.today()
    date_plus_week = current_date + timedelta(weeks=1)

    for user in users:

        birthday_date = date(current_date.year, user['birthday'].date().month, user['birthday'].date().day)
        
        if current_date <= birthday_date < date_plus_week:
            if birthday_date.strftime('%A') in WEEKEND:
                if BIRTHDAY_WEEK['Monday']:
                    BIRTHDAY_WEEK['Monday'] += f", {user['name']}"
                else:
                    BIRTHDAY_WEEK['Monday'] = user['name']
            else:
                if BIRTHDAY_WEEK[birthday_date.strftime('%A')]:
                    BIRTHDAY_WEEK[birthday_date.strftime('%A')] += f", {user['name']}"
                else:
                    BIRTHDAY_WEEK[birthday_date.strftime('%A')] = user['name']

    for num in range(7):

        number_week_day = date(current_date.year, current_date.month, current_date.day) + timedelta(days=num)
        week_day = number_week_day.strftime('%A')

        if not week_day in WEEKEND and BIRTHDAY_WEEK[week_day]:
            print(f'{week_day}: {BIRTHDAY_WEEK[week_day]}')

