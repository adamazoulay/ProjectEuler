
if __name__=="__main__":
    cur_day = 1
    year = 1901

    # Find the day number for all first days of the month
    first_days = [1]
    while year < 2001:
        cur_day += 31  # January
        first_days.append(cur_day)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            feb = 29
        else:
            feb = 28
        cur_day += feb
        first_days.append(cur_day)
        cur_day += 31  # March
        first_days.append(cur_day)
        cur_day += 30  # April
        first_days.append(cur_day)
        cur_day += 31  # May
        first_days.append(cur_day)
        cur_day += 30  # June
        first_days.append(cur_day)
        cur_day += 31  # June
        first_days.append(cur_day)
        cur_day += 31  # August
        first_days.append(cur_day)
        cur_day += 30  # September
        first_days.append(cur_day)
        cur_day += 31  # October
        first_days.append(cur_day)
        cur_day += 30  # November
        first_days.append(cur_day)
        cur_day += 31  # December
        first_days.append(cur_day)
        year += 1

    first_days.pop()
    max = first_days[-1]
    sundays = 7
    total = 0
    while sundays < max:
        if sundays in first_days:
            total += 1
        sundays += 7


    print(total - 2) # -2 for first year, 1900
