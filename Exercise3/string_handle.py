def is_palindrome(word):
    return word[0:] == word[::-1]


def find_frequent_letter_and_digit(word):
    word = word.upper()
    word_frequency = dict()

    for w in word:
        if w.isdigit() or w.isalpha():
            if w not in word_frequency:
                word_frequency[w] = 1
            else:
                word_frequency[w] = word_frequency[w] + 1

    word_maximum_frequency = [word[0] for word in word_frequency.items() if word[1] == max(word_frequency.values())]

    return word_maximum_frequency


def count_letter_space_digit(word):
    word_count_dict = {"letter": 0, "space": 0, "digit": 0}
    for w in word:
        if w.isalpha():
            word_count_dict["letter"] = word_count_dict["letter"] + 1
        elif w.isspace():
            word_count_dict["space"] = word_count_dict["space"] + 1
        elif w.isdigit():
            word_count_dict["digit"] = word_count_dict["digit"] + 1
        else:
            continue
    return word_count_dict


if __name__ == "__main__":
    print(is_palindrome("radar"))
    print(is_palindrome("a"))
    print(is_palindrome("abc"))

    print(find_frequent_letter_and_digit("hjklTttTT233333@@@@@กกกกก"))

    print(count_letter_space_digit("gg  1234556   $$$"))
