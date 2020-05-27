import calendar

def day_from_date (date):
    day, month, year = date.split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    day_num = calendar.weekday(year, month, day)
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days_of_week[day_num]

def number_to_words_date (date):
    day, month, year = date.split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    day_num = calendar.weekday(year, month, day)
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    date_ending = {
        1: "st",
        2: "nd",
        3: "rd",
        5: "th",
        6: "th",
        7: "th",
        8: "th",
        9: "th",
        10: "th",
        11: "th",
        12: "th",
        13: "th",
        14: "th",
        15: "th",
        16: "th",
        17: "th",
        18: "th",
        19: "th",
        20: "th",
        21: "st",
        22: "nd",
        23: "rd",
        24: "th",
        25: "th",
        26: "th",
        27: "th",
        28: "th",
        29: "th",
        30: "th",
        31: "st",

    }


    return [days_of_week[day_num], str(day) + date_ending[day], months[month], year]