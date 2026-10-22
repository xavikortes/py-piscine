def count_harvest(current_day: int, harvest_day: int):
    print(f"Day {current_day}")

    if current_day == harvest_day:
        print("Harvest time!")
    else:
        count_harvest(current_day + 1, harvest_day)


def ft_count_harvest_recursive():
    harvest_day = input("Days until harvest: ")
    count_harvest(1, int(harvest_day))
