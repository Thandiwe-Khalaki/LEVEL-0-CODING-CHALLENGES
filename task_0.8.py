def number_to_time(number):

    hour = number // 60
    minutes = number % 60
    
    if hour < 1 and minutes < 1:
        return (str(hour) + " hour," + str(minutes) + " minute")
    elif hour <= 1:
        return (str(hour) + " hour," + str(minutes) + " minutes")
    elif minutes <= 1:
        return (str(hour) + " hour," + str(minutes) + " minute")
    else:
        return (str(hour) + " hour," + str(minutes) + " minutes")



print(number_to_time(133))