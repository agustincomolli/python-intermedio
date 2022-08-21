def run():
    my_list = [1, "Hola", True, 3.2]
    my_dict = {"nombre": "Agustín", "apellido": "Comolli"}
    super_list = [
        {"nombre": "Agustín", "apellido": "Comolli"},
        {"nombre": "Carlos", "apellido": "Giola"},
        {"nombre": "Adrián", "apellido": "Gomez"},
        {"nombre": "Lorena", "apellido": "Mellado"}
    ]
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)


if __name__ == "__main__":
    run()
