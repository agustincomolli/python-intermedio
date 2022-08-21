from turtle import width


def read():
    numbers = []
    with open("./files/numbers.txt", mode="r", encoding="UTF-8") as file:
        for line in file:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Agustín", "Lorena", "Carlitos", "Marcela", "Adrián"]
    # Crer un archivo nuevo o sobreescribir el existente.
    with open("./files/names.txt", mode="w", encoding="UTF-8") as file:
        for name in names:
            file.write(name + "\n")
    # Agregar datos al archivo sin sobreescribirlo.
    with open("./files/names.txt", mode="a", encoding="UTF-8") as file:
        file.write("Gustavo")


def run():
    read()
    write()


if __name__ == "__main__":
    run()
