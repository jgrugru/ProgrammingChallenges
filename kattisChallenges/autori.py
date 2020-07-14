import sys
abbreviation = ""
for i in sys.stdin:
    # i.rstrip()
    for x in i:
        if x.isupper():
            abbreviation += x
        elif x == '\n':
            print(abbreviation)
            abbreviation = ''

