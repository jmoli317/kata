def build(number_of_floors: int):
    return [
        ("*" * (i * 2 - 1)).center(number_of_floors * 2 - 1)
        for i in range(1, number_of_floors + 1)
        ]
