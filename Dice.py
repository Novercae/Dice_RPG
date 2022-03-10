from random import randint


def dice():
    print("Type: D-4, D-6, D-8, D-10, D-20, D-100")
    x = input(">>> ").upper()

    if x == "D-4":
        d_4 = randint(1, 4)
        return print(f"Dice roll: {d_4}")
    if x == "D-6":
        d_6 = randint(1, 6)
        return print(f"Dice roll: {d_6}")
    if x == "D-8":
        d_8 = randint(1, 8)
        return print(f"Dice roll: {d_8}")
    if x == "D-10":
        d_10 = randint(1, 10)
        return print(f"Dice roll: {d_10}")
    if x == "D-20":
        d_20 = randint(1, 20)
        return print(f"Dice roll: {d_20}")
    if x == "D-100":
        d_100 = randint(1, 100)
        return print(f"Dice roll: {d_100}")
    else:
        print('Not a dice number.')


if __name__ == '__main__':
    while 1:
        dice()
        print()
