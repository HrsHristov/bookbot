def main():
    book_path ="./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found '{item['num']}' times")

    print("--- End report ---")

def count_words(text):
    words = text.split()
    words_count = len(words)
    return words_count

def count_chars(text):
    chars = {}
    formatted_text = text.lower();

    for char in formatted_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()