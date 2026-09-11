# count all words
def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

# count all characters
def count_characters(file_contents):
    character_counts = {}
    for character in file_contents:
        character_counts[character.lower()] = character_counts.get(character.lower(), 0) + 1
    return character_counts

# target specific characters
def get_target_counts(text, chars):
    character_counts = count_characters(text)
    target = {}
    for char in chars:
        target[char] = character_counts[char]
    return target

# sort with key
def sort_on(character: tuple[str, int]) -> int:
    return character[1]

# sort dictionary
def chars_dict_to_sorted_list(character_counts: dict[str, int]) ->list[tuple[str, int]]:
    sorted_list = sorted(character_counts.items(), reverse=True, key=sort_on)
    return sorted_list

# extracting alpha characters only
def alpha_only(character_counts):
    sorted_list = chars_dict_to_sorted_list(character_counts)
    alphas= []
    for item in sorted_list:
        if item[0].isalpha():
            alphas.append(item)
    return alphas