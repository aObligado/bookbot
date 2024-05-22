
def main(): 
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words_count = get_num(text)
    lower_text = get_lower_case(text)
    letter_count = get_letter_num(lower_text)
    to_list(letter_count)
    #print(words_count)
    #print(letter_count)

def get_num(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_lower_case(text):
    return text.lower()

def get_letter_num(text):
    letter_num = dict()
    for letter in text:
        if letter not in letter_num:
            letter_num[letter] = 1
        else:
            letter_num[letter] = letter_num[letter] + 1
    return letter_num

def to_list(dictionary):
    character_times = []
    for key, value in dictionary.items():
        character_times.append({'character': key, 'times': value})
    character_times.sort(reverse=True, key=lambda d: d['times'])
    print(character_times)
    return character_times
main()