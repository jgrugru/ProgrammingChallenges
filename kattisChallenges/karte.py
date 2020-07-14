import sys
for i in sys.stdin:
    i = i.rstrip()
    greska = False           
    count = 0
    cardsList = []
    pcount = 0
    hcount = 0
    kcount = 0
    tcount = 0
    while True:
        try:
            if i[count:count+3] in cardsList:
                greska = True
                print('GRESKA')
                break
            elif i[count] == 'P':
                pcount += 1
            elif i[count] == 'K':
                kcount += 1
            elif i[count] == 'H':
                hcount += 1
            elif i[count] == 'T':
                tcount += 1
            cardsList.append(i[count:count+3])
        except (IndexError):
            if not greska:
                print(13-int(pcount),13-int(kcount),13-int(hcount),13-int(tcount))
            break
        count += 3
