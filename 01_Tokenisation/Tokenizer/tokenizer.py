import sys, re

abbr = ['etc.', 'e.g.', 'i.e.']

def tokenize (line, abbr):
    line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
    line = re.sub(r'([^0-9]),', r'\g<1> ', line)
    line = re.sub(r'([^0-9]),', r' \g<1> ', line)
    line = re.sub(r'  +', ' ', line[:-1])

    output  = []
    for token in line.split(' '):
        if len(token) == 0: continue
        if token[-1] == '.' and token not in abbr:
            token = token[:-1] + " ."
        output.append(token)
    return " ".join(output)

#line = sys.stdin.readline()

def maxMatch (text, dictionary):
    if text == "": return []
    if len(text) == 1: return [text]

    for i in range(1, len(text)):
        firstword = text[:i]
        remainder = text[i:]
        if firstword in dictionary:
            return [firstword] + maxMatch (remainder, dictionary)
    return []

dictionary = set(["a","b", "c","d"])
print(maxMatch ("abdbc", dictionary))

#while line != '':
    #print(tokenize(line.strip('\n'), abbr))
    #line = sys.stdin.readline()
