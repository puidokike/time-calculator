def add_time(start, duration, weekday=False):

    # "start" time conversion:
    hours_str, minutes_str = map(int, start.split()[0].split(":"))
    hours, minutes = hours_str, minutes_str

    # "duration" time conversion:
    dur_hours_str, dur_minutes_str = map(int, duration.split()[0].split(":"))
    dur_hours, dur_minutes = dur_hours_str, dur_minutes_str

    result_hour = hours + dur_hours
    result_min = minutes + dur_minutes

    days = 0
    period = ""
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday", "Sunday")

    # converting to 24-hour clock format
    if "PM" in start and hours != 12:
        result_hour += 12

    # minutes to hours if minutes >= 60
    if result_min >= 60:
        hours_add = result_min // 60
        result_min -= hours_add * 60
        result_hour += hours_add

    # hours to days if hours >= 24
    if result_hour > 24:
        days = result_hour // 24
        result_hour -= days * 24

    # checking if result time "AM" or "PM":
    if 0 < result_hour < 12:
        period = "AM"
    elif result_hour == 12:
        if "AM" in start:
            period = "PM"
        else:
            period = "AM"
    elif result_hour > 12:
        period = "PM"
        result_hour -= 12
    elif result_hour == 0:
        period = "AM"
        result_hour += 12

    if days > 0:
        if days == 1:
            days_later = " (next day)"
        else:
            days_later = f" ({days} days later)"
    else:
        days_later = ""

    if weekday:
        weeks = days // 7
        index = weekdays.index(weekday.lower().capitalize()) + (days - 7 * weeks)
        if index > 6:
            index -= 7
        day = f", {weekdays[index]}"
    else:
        day = ""

    # formatting minutes if 0 < minutes < 10:
    if result_min < 10:
        result_min = f"0{result_min}"

    # final time stamp:
    new_time = f"{result_hour}:{result_min} {period}{day}{days_later}"

    return new_time
