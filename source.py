import sys
import itertools
import operator


def read_file():
    rack_letters = []
    filepath = 'sowpods.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            rack_letters.append((line.strip()).lower())
            line = fp.readline()
    return rack_letters


def scrabble_score(word):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    total = 0
    for letter in word:
        total += scores[letter]
    return total


def count_scores(valid_word_list):
    mylist = []
    count = 0
    for word in valid_word_list:
        score = scrabble_score(word)
        mylist.append([])
        mylist[count].append(word)
        mylist[count].append(score)
        count = count+1
    score_sort = sorted(mylist, key = operator.itemgetter(1), reverse=True)
    for value in score_sort:
        print value


def find_valid_words(
        word_list,
        rack_letters
        ):
    valid_word_list = []
    for word in word_list:
        for rack in rack_letters:
            if word == rack:
                # print(word + "-----" + rack)
                valid_word_list.append(rack)
    count_scores(valid_word_list)


def make_comb(chars):
    word_list = []
    for x in range(1, len(chars)+1):
        t = list(itertools.permutations(chars, x))
        for i in range(0, len(t)):
            word_list.append(''.join(t[i]))
    return word_list


def read_cmd_arg():
    if len(sys.argv) < 2:
        print('Argument Is Missing')
    else:
        return make_comb((str.lower((sys.argv[1]))))


word_list = read_cmd_arg()
rack_letters = read_file()
find_valid_words(word_list, rack_letters)
