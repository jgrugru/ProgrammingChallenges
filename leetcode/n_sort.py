from math import ceil
def simpleSort(myList, n: int):
    if n == 0 or n==1:
        myList.sort()
        return myList
    else:
        new_list = []
        for sub_list_index in range(ceil(len(myList)/n)):
            sub_list = myList[(sub_list_index) * n:(sub_list_index + 1) * n]
            sub_list.sort()
            for digit in sub_list:
                if digit:
                    new_list.append(digit)
        return new_list
                

print(simpleSort([4, 2, 5, 6, 3, 1, 3, 2, 5], 0))
print(simpleSort([4, 2, 5, 6, 3, 1, 3, 2, 5], 1))
print(simpleSort([4, 2, 5, 6, 3, 1, 3, 2, 5], 2))
print(simpleSort([4, 2, 5, 6, 3, 1, 3, 2, 5], 3))
