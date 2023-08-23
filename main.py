def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text_from_path(book_path)
    number_of_words = get_number_of_words(book_text)
    # print(f"number of words: {number_of_words}")
    char_count_dict = get_char_count(book_text)
    # print(f"char count dict: {char_count_dict}")
    get_report(book_path, number_of_words, char_count_dict)

def get_book_text_from_path(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    lowered = text.lower()
    for char in lowered:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_report(book_path, num_words, char_count):
    sorted_char_count = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    sorted_char_count_dict = dict(sorted_char_count)
    # print(sorted_char_count_dict)
        
    print(f"--- Begin report of {book_path} ---")
    
    for k, v in sorted_char_count_dict.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
            
    print("--- End report ---")
            
main()