import sys
for i in sys.stdin:
    numberOfStatues = int(i.rstrip())
    min = 0
    # for numberOfPrinters in range(1,numberOfStatues+1):
    #     for days in range(1,numberOfStatues+1):
    #         print("day", days," -- ", numberOfPrinters, " printers")
    #         if(days * numberOfPrinters >= numberOfStatues):
    #             print("the min is", days)
    #             # min = days
    #             break
    for days in range(0, numberOfStatues + 1):
        numberOfPrinters = 2 ** days
        print("day", days," -- ", numberOfPrinters, " printers")
        for x in range(1, numberOfStatues+1):
            if(x * numberOfPrinters >= numberOfStatues):
                    print("the min is", x)
                    # min = days
                    break
    
    print(min)