import sys


def read_file(chars_list):
    """
    reads file sowpods.txt line by line
    returns list of strings
    """
    rack_letters = []
    filepath = 'sowpods.txt'
    with open(filepath) as fp:
        line = fp.readline()
        word = (line.strip()).lower()
        while line:
            for char in chars_list:
                if char in word:
                    rack_letters.append((line.strip()).lower())
            line = fp.readline()
    return rack_letters


def scrabble_score(word):
    """
    checks score of single valid word
    return score
    """
    scores_list = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                   "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                   "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                   "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                   "x": 8, "z": 10}
    total_score = 0
    for letter in word:
        total_score += scores_list[letter]
    return total_score


def print_scrable_list(scrable_list):
    """
    print sorted scrable_list
    """
    for scrable_pair in scrable_list:
        print (scrable_pair)
    exit()  # exiting the program


def count_scores(valid_word_list):
    """
    takes valid _word_list
    calls scrabble_score method
    makes 2d list of word and scores
    sorts scrable_list
    """
    scrable_list = []
    world_count = 0
    for word in valid_word_list:
        world_score = scrabble_score(word)
        scrable_list.append([])
        scrable_list[world_count].append(world_score)
        scrable_list[world_count].append(word)
        world_count = world_count+1
    print_scrable_list(sorted(scrable_list, reverse=True))


def match_word(
        chars_list,
        rack_word
        ):
    for rack_char in rack_word:
        if rack_char not in chars_list:
            return False
        if chars_list.count(rack_char) < rack_word.count(rack_char):
            return False
    return True


def find_valid_words(
        chars_list,
        rack_letters
        ):
    """
    match all combinations of word_list
    with given dataset
    """
    valid_word_list = []
    for rack in rack_letters:
        if match_word(chars_list, rack):
            valid_word_list.append(rack)
    count_scores(valid_word_list)


def read_cmd_arg():
    """
    reads cmd line args
    """
    if len(sys.argv) < 2:
        print('Argument Is Missing')
        exit()  # exiting program
    else:
        return str.lower((sys.argv[1]))


chars_list = read_cmd_arg()
rack_letters = read_file(chars_list)
find_valid_words(chars_list, rack_letters)
