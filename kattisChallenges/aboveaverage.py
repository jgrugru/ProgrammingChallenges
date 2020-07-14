import sys
count = 0
key = ''
mystring=''
for i in sys.stdin:
    listofinput = []
    i = int(i.rstrip())
    outputList = []
    for x in range(i):
        testinput = input()
        testinput = testinput.split(' ')
        sumOfTestScores = 0
        listOfTestScores = []
        for testscore in testinput[1:]:
            listOfTestScores.append(int(testscore))
            sumOfTestScores += int(testscore)
        average = sumOfTestScores / len(listOfTestScores)
        countAboveAverage = 0
        for testscore in listOfTestScores:
            if testscore > average:
                countAboveAverage += 1
        aboveAveragePercentage = float(countAboveAverage/len(listOfTestScores)) * 100
        outputList.append("{:.3f}%".format(aboveAveragePercentage))
    for percentage in outputList:
        print(percentage)