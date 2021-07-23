from collections import defaultdict
from math import ceil

def convert_dict_to_str(my_dict):
    return_str = ""
    for str_list in my_dict.values():
        for char in str_list:
            return_str += char

    return return_str

def convert(s: str, numRows: int) -> str:
    if numRows >= len(s) or numRows == 1:
        return s

    column_gap = numRows - 2
    output_dict = defaultdict(list)
    starting_index = numRows + column_gap
    if numRows - column_gap  == 2:
        num_columns = ceil(len(s)/numRows)
    else:
        num_columns = int(len(s)/numRows)

    for count in range(num_columns):
        # breakpoint()
        if count == 0:
            col_str = s[0:starting_index]
        else:
            col_str = s[(starting_index * count):(starting_index * (count + 1))]

        for index, char in enumerate(col_str[:numRows]):
            output_dict[index].append(char)

        for index, char in enumerate(col_str[numRows:]):
            output_dict[(numRows - 2) - index].append(char)

    
    return convert_dict_to_str(output_dict)


print(convert("PAYPALISHIRING", 2))
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("PAYPALISHIRING", 5))
print(convert("knnnnnnnnnnnnnvckjlhaj", 100))
print(convert("AB", 1))
print(convert("AB", 2))
print(convert("ABC", 2))
print(convert("ABCDE", 3))
print(convert("PAYPALI", 4))

