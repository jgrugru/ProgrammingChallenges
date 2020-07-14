import sys
outputlist = []
for i in sys.stdin:
    i = i.rstrip()
    i = i.split(' ')
    numerator = int(i[0])
    denominator = int(i[1])
    if numerator != 0 and denominator != 0:
        intDivideByDenominator = int(numerator/denominator)
        remainderDivideByDenominator = numerator % denominator
        outputstring = str(intDivideByDenominator) + ' ' + str(remainderDivideByDenominator) + ' / ' + str(denominator)
        outputlist.append(outputstring)
    else:
        break
for x in outputlist:
    print(x)