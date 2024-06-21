def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_number_words(text)
    count_chars = count_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document\n\n")
    list = dict_to_list(count_chars)
    list.sort(reverse=True, key=sort_on)
    for item in list:
        if item['char'].isalpha():
            print(f"The {item['char']} character was found {item['count']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_words(book):
    words = book.split()
    return(len(words))

def count_char(book):
    lowered_book = book.lower()
    counts = {}
    for char in lowered_book:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def dict_to_list(d):
    list = []
    for key, value in d.items():
        list.append({'char': key, 'count': value})
    return list

def sort_on(d):
    return d['count']

main()
