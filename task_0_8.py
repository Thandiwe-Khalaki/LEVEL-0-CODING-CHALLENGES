def number_to_time(number):

    hours = int(number / 60)
    minutes = number % 60

    if hours > 1 and minutes > 1:
        print(f"{hours} hours, {minutes} minutes")
    elif hours < 2 and minutes > 1:
        print(f"{hours} hour, {minutes} minutes")
    elif hours == 0 and minutes == 0:
        print(f"{hours} hours, {minutes} minutes")
    elif hours > 1 and minutes < 2:
        print(f"{hours} hours, {minutes} minute")
    else:
        print(f"{hours} hour, {minutes} minute")


number_to_time(0)
