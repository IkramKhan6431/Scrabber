import sys
import operator

SCORES_LIST = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
               "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
               "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
               "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
               "x": 8, "z": 10}


def find_valid_word_list(rack_chars_list):
    """
    reads file sowpods.txt line by line
    returns list of valid strings (valid_word_list)
    """
    valid_word_list = []
    filepath = 'sowpods.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if match_word(rack_chars_list, (line.strip()).lower()):
                valid_word_list.append((line.strip()).lower())
            line = fp.readline()
    return valid_word_list


def match_word(rack_chars_list, rack_word):
    """
    match rack_word with given rack_chars_list
    """
    for rack_char in rack_word:
        if rack_char not in rack_chars_list:
            return False
        if rack_chars_list.count(rack_char) < rack_word.count(rack_char):
            return False
    return True


def compute_scrabble_word_score(word):
    """
    compute score of single valid word
    return score
    """
    global SCORES_LIST
    total_score = 0
    for letter in word:
        total_score += SCORES_LIST[letter]
    return total_score


def compute_scrabble_list_scores(scrable_word_list):
    """
    takes valid_word_list
    calls compute_scrabble_word_score method
    makes dictionary of word and scores
    sorts scrable_word_collection
    return scrable_word_collection
    """
    scrable_word_collection = {}
    for word in scrable_word_list:
        word_score = compute_scrabble_word_score(word)
        scrable_word_collection[word] = word_score
    sorted_scrable_word_list = sorted(scrable_word_collection.items(),
                                      key=operator.itemgetter(1), reverse=True)
    return sorted_scrable_word_list


def print_scrable_list(scrable_word_list):
    """
    print sorted scrable_list
    """
    for scrable_pair in scrable_word_list:
        print (str(scrable_pair[1]) + ",   " + scrable_pair[0])


def read_cmd_arg():
    """
    reads cmd line args
    """
    if len(sys.argv) < 2:
        print('Argument Is Missing')
        exit()  # exiting program
    else:
        return str.lower((sys.argv[1]))

if __name__ == "__main__":
    rack_chars_list = read_cmd_arg()
    scrable_word_list = find_valid_word_list(rack_chars_list)
    sorted_scrable_word_list = compute_scrabble_list_scores(scrable_word_list)
    print_scrable_list(sorted_scrable_word_list)
