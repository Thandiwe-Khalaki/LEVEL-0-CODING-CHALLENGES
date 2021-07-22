def number_to_time(number):

    minutes = number - (60 * (number // 60))
    hours = number // 60

    if minutes > 1 and hours > 1:
        print(f"{hours} hours {minutes} minutes")
    elif hours == 1 and minutes > 1:
        print(f"{hours} hour {minutes} minutes")
    elif minutes == 1 and hours > 1:
        print(f"{hours} hours {minutes} minutes")
    elif hours <= 1 and minutes > 1:
        print(f"{hours} hour {minutes} minutes")
    else:
        print(f"{hours} hour, {minutes} minute")


number_to_time(61)
