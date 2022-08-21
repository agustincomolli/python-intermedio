def divisors(num):
    try:
        if num < 0:
            raise ValueError("negative")
        return [i for i in range(1, num + 1) if num % i == 0]
    except ValueError:
            print("Debe ingresar un número mayor a 0.")


def main():
    try:
        num = int(input("Escribe un número: "))
        print(divisors(num))
        print("Terminó el programa.")
    except ValueError:
        print("Debe ingresar un número entero.")


if __name__ == "__main__":
    main()
