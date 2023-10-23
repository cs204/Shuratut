while True:
    fuel_input = input("Дробь: ")
    try:
        x, y = list(map(int, fuel_input.split("/")))
        if x > y:
            raise ValueError
        volume = int((x / y) * 100)
        if volume <= 1:
            print("E")
        elif volume >= 99:
            print("F")
        else:
            print(f"{volume}%")
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
