from turtle import width


def read():
    numbers = []
    with open("./files/numbers.txt", mode="r", encoding="UTF-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)


def write():
    pass


def main():
    read()


if __name__ == "__main__":
    main()
