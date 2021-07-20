def number_to_time(number):

    hours = number // 60
    minutes = number % 60
    
    if hours < 1 and minutes < 1:
        return (str(hours) + " hour, " + str(minutes) + " minute")
    elif hours <= 1:
        return (str(hours) + " hour, " + str(minutes) + " minutes")
    elif minutes <= 1:
        return (str(hours) + " hours, " + str(minutes) + " minute")
    else:
        return (str(hours) + " hours, " + str(minutes) + " minutes")


print(number_to_time(133))