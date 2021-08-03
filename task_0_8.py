def number_to_time(number):
    minute = int(number % 60)
    hour = int(number // 60)

    minutes = "minute" if (minute == 1) else "minutes"
    hours = "hour" if (hour == 1) else "hours"
    print(f"{int(number//60)} {hours}, {int(number%60)} {minutes}")


def main():
    number_to_time(1)

if __name__ == "__main__":
    main()
