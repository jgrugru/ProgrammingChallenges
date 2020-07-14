import sys
for i in sys.stdin:
    i = i.rstrip()
    i = i.split(' ')
    print(abs(int(i[0]) - int(i[1])))