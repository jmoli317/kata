def to_camel_case(text):
    camel_case_text = ""
    bad_chars = ["_", "-"]
    char_index = 0

    for char in text:
        if char in bad_chars:
            camel_case_text += text[char_index + 1].upper()
        elif text[char_index - 1] in bad_chars:
            pass
        else:
            camel_case_text += char
        char_index += 1
    return camel_case_text
