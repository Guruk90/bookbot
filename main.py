def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = get_words_count(text)
    chars = get_char_count(text)
    sorted_chars = get_sorted_char_list(chars)
    # print(f"number of words: {count}")
    # print(get_sorted_char_list(chars))
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count} words found in the document\n")
    char_dicts(sorted_chars)
    print("--- End report ---")


def char_dicts(sorted_chars):
    for char in sorted_chars:
        print(f"The {char["char"]} character was found {char["value"]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words_count(text):
    words = text.split()
    nummer_of_words = len(words)
    return nummer_of_words


def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["value"]


def get_sorted_char_list(chars):
    sorted_chars = []
    for c in chars:
        if c.isalpha():
            sorted_chars.append({"char": c, "value": chars[c]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


main()
