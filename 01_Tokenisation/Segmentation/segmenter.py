import sys
import nltk.data


def followed_by_upper_case():
    line = sys.stdin.readline()
    while line != '':
        end_found = False
        beginning = 0
        for index, character in enumerate(line):
            if character == " ": 
                continue
            if character in ".,?!": 
                end_found = True
                end = index + 1
                continue
            if end_found and character.isupper():
                sys.stdout.write(line[beginning:end] + "\n")
                beginning  = index
                end_found = False
            elif end_found:
                end_found = False
            
        sys.stdout.write(line[beginning:])
        line = sys.stdin.readline()


def punkt_version():
    line = sys.stdin.readline()
    text = ""
    while line != '':
        text += line
        line = sys.stdin.readline()

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sys.stdout.write('\n'.join(sent_detector.tokenize(text.strip())))
    line = sys.stdin.readline()

if len(sys.argv) != 2:
    print("usage: 'python3 segmenter.py [case/punkt] < textfile'")
    exit()

if sys.argv[1] == "case":
    followed_by_upper_case()
    exit()
elif sys.argv[1] == "punkt":
    punkt_version()
    exit()
else:
    print("Invalid option: 'python3 segmenter.py' to see usage\n")
    exit()
