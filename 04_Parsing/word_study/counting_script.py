import sys

if len(sys.argv) != 2: 
    print("Usage: python counting_script.py language_name [stdin <- UD_File]")
    exit()

v_found = 0
verb_counter = 0
vo_counter = 0

line = sys.stdin.readline()

while line != '':
    line = sys.stdin.readline()

    if line == "\n":
        v_found = 0

    if "VERB" in line:
        if v_found == 1:
            verb_counter += 1
            continue

        else:
            v_found = 1
            continue

    if "obj" in line:
        if v_found == 1:
            vo_counter += 1
            verb_counter += 1
            v_found = 0
        else:
            continue

print(sys.argv[1], verb_counter, vo_counter)
