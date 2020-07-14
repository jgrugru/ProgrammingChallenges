import sys
count = 0
key = ''
mystring=''
for i in sys.stdin:
    count += 1
    i = i.rstrip()
    if count == 1:
        encrypted = i
    elif count == 2:
        key = i
        outputstr = ''
        for count, char in enumerate(key):
            myasciicode = ord(encrypted[count])
            moveunits = ord(char)-65
            if count % 2 == 0 or count == 0:
                if(myasciicode - moveunits < 65):
                    moveunits = 64 - (myasciicode - moveunits)
                    myasciicode = 90
                # print("Move ", encrypted[count], "(", myasciicode, ")", ":", moveunits, " counts to the left")
                outputstr += str(chr(myasciicode - moveunits))
            else:
                if(myasciicode + moveunits > 90):
                    moveunits = (myasciicode + moveunits) - 91
                    myasciicode = 65
                # print("Move ", encrypted[count], "(", myasciicode, ")", ":", moveunits, " counts to the right")
                outputstr += str(chr(myasciicode + moveunits))

        print(outputstr)
        count = 0
        key = ''
        mystring=''
    


            # if count % 2 == 0 or count == 0:
            #     if((mystringord - difference) < 65):
            #         difference = mystringord + difference - 65 - 1
            #         mystringord = 90
            #     # print(mystringord, difference)
            #     outputstr = outputstr + str(chr(int(mystringord) - difference))
            # else:
            #     if((mystringord + difference) > 90):
            #         difference = mystringord + difference - 90 - 1
            #         mystringord = 65
            #     # print(mystringord, difference)
            #     outputstr = outputstr + str(chr(int(mystringord) + difference))