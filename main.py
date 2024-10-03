def main():
    book_path ="./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)

    print(f"{num_words} words found in the document")
    print(chars_dict)

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

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()