def intToRoman(num: int) -> str:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}
    roman_numeral_list = list(reversed(roman_numerals.keys()))
    remainder = num
    returning_str = ""
    previous_quotient = 0

    for count, letter in enumerate(reversed(roman_numerals)):
        quotient, remainder = divmod(remainder, roman_numerals[letter])

        if quotient == 4:
            if previous_quotient:
                returning_str = returning_str[0:len(returning_str)-1] + letter + roman_numeral_list[count - 2]
            else:
                returning_str = returning_str[0:len(returning_str)] + letter + roman_numeral_list[count - 1]
        else:
            for x in range(quotient):
                returning_str += letter
           
        previous_quotient = quotient

    return returning_str


print(f"{intToRoman(999)}\nCMXCIX")
print(f"{intToRoman(3999)}\nMMMCMXCIX")
print(f"{intToRoman(499)}\nCDXCIX")
