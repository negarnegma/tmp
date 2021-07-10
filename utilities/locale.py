def convert_letters_from_arabic_to_persian(s):
    letter_map = {
        "ك": "ک",
        "ي": "ی",
    }

    for letter in letter_map:
        s = s.replace(letter, letter_map[letter])

    return s
