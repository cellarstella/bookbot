import sys
from stats import word_count, sort_char_count

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = word_count(text)
        character_dict = sort_char_count(text)
        print_report(sys.argv[1], num_words, character_dict)
        sys.exit(0)

def get_book_text(f):
    with open (f) as f:
        return f.read()
    
def print_report(file, num_words, dict):
    print(f'============ BOOKBOT ============\nAnalyzing book found at {file}...\n')
    print(f'----------- Word Count -----------\nFound {num_words} total words\n')
    print(f'--------- Character Count ---------')
    for char in dict:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print('============= END ===============')

main()
