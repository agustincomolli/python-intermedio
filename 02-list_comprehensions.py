def challenge():
    # Crear una lista de 5 dígitos con todos los múltiplos de 4 que a su vez
    # sean múltiplos de 6 y de 9.
    challenge_list = [
        i * 4 for i in range(1, 100000) if (i % 6 == 0) and (i % 9 == 0)]
    print(challenge_list)


def main():
    squares = []

    # Crear una lista de 100 números enteros elevados al cuadrado y que no
    # sean divisibles por 3.
    for i in range(1, 101):
        if not i % 3 == 0:
            squares.append(i**2)

    # Nueva forma de crear la lista pero con list comprehensions.
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)
    challenge()


if __name__ == "__main__":
    main()
