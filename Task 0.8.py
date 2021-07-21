def number_to_time(number):

    hours = number // 60
    minutes = number % 60
    
    if hours < 1 and minutes < 1:
       print((str(hours) + " hour, " + str(minutes) + " minute"))
    elif hours <= 1:
        print((str(hours) + " hour, " + str(minutes) + " minutes"))
    elif minutes <= 1:
        print((str(hours) + " hours, " + str(minutes) + " minute"))
    else:
        print((str(hours) + " hours, " + str(minutes) + " minutes"))


number_to_time(2)
number_to_time(71)
number_to_time(173)
number_to_time(0)