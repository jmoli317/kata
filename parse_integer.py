def parse_int(string: str):
    """
    Return the spelled-out number in integer form.

    Example:
    "one hundred and twenty-five" -> 125

    :param string: A number spelled in English.
    :return: The integer form of the entered string's number.
    """
    num_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        }
    cleaned_str = string.replace(" and", "")
    integers = []
    for num in cleaned_str.split():
        ops = []
        indices = []
        if num in ["hundred", "thousand", "million"]:
            for i, integer in enumerate(integers):
                if integer < num_words[num]:
                    indices.append(i)
                    ops.append(integer)
            for i in indices:
                integers[i] = 0
            integers.append(sum(ops) * num_words[num])
        else:
            if "-" in num:
                parts = num.split("-")
                integers.append(sum([num_words[part] for part in parts]))
            else:
                integers.append(num_words[num])
    return sum(integers)
