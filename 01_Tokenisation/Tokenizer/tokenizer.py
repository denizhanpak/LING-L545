import sys, re

if len(sys.argv) < 2:
    print("Usage: python tokenizer.py dictionary document [stdin document to tokenize]")
    exit()

def maxMatch (text, dictionary):
    if len(text) <= 1: return [text]

    for i in range(1, len(text)):
        firstword = text[:i]
        remainder = text[i:]
        if firstword in dictionary:
            return [firstword] + maxMatch (remainder, dictionary)
    return []

dictfile = open(sys.argv[1], 'r')
dictionary = [line.strip("\n") for line in dictfile.readlines()]

line = sys.stdin.readline()
while line != '':
    print(maxMatch(line.strip('\n'), dictionary))
    line = sys.stdin.readline()

