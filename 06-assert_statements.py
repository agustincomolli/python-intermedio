def divisors(num):
    if num < 0:
        raise ValueError("negative")
    return [i for i in range(1, num + 1) if num % i == 0]


def run():
    num = input("Escribe un número: ")
    assert num.isnumeric(), "Debe ingresar un número."
    print(divisors(int(num)))
    print("Terminó el programa.")


if __name__ == "__main__":
    run()
