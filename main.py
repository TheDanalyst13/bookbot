import sys

# getting analysis component
from stats import count_words, count_characters, get_target_counts, chars_dict_to_sorted_list, alpha_only

# checking for proper number of command arguments
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# request path
def request_path() -> str:
    path = sys.argv[1]
    return path

# open file, get contents, save to variable
def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents

path = request_path()
text = get_book_text(path)
character_counts = count_characters(text)

#making report
def print_report(path, count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, num in sorted_list:
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

print_report(path, count_words(text), chars_dict_to_sorted_list(character_counts))