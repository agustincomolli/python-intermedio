def challenge():
    # Crear un diccionario con los primeros 1000 números naturales y su clave
    # sea su raíz cuadrada.
    my_dict = {i: round(i ** 0.5, 2) for i in range(1, 1001)}
    print(my_dict)


def main():
    challenge_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            challenge_dict[i] = i ** 3

    print(challenge_dict)

    dic_comprehension = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(dic_comprehension)

    print("\nDesafío:")
    challenge()


if __name__ == "__main__":
    main()
