import sys
count = 0
L,D,X = 0,0,0
for i in sys.stdin:
    i = i.rstrip()
    count += 1
    if count == 1:
        L = int(i)
    elif count == 2:
        D = int(i)
    elif count == 3:
        X = int(i)
        listOfPossibleNumbers = []

        ###Find highest and lowest sum of digits brute force method
        while L <= D:
            strx = str(L)
            sumOfDigits = 0
            for digit in strx:
                sumOfDigits += int(digit)
            if sumOfDigits == X:
                listOfPossibleNumbers.append(L)
            L+= 1
        if(len(listOfPossibleNumbers)>0):
            print(listOfPossibleNumbers[0])
            print(listOfPossibleNumbers[len(listOfPossibleNumbers)-1])
        ############################################


        count = 0

