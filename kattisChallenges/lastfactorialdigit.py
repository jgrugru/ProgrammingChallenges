import sys
count = 0
key = ''
mystring=''
for i in sys.stdin:
    listofnvalues = []
    i = int(i.rstrip())
    for x in range(i):
        getnvalue = input()
        listofnvalues.append(int(getnvalue))
    for n in listofnvalues:
        if n != 0:
            factorial = 1
        else:
            factorial = 0
        for x in range(1,n+1):
            factorial = factorial * x
        factorial = str(factorial)
        print(factorial[len(factorial)-1])