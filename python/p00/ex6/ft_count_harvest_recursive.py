def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_days(1, days)


def print_days(day, total):
    if day > total:
        print("Harvest time!")
    else:
        print(f"Day {day}")
        print_days(day + 1, total)

# ft_count_harvest_recursive()
