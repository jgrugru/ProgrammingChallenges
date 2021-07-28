def intToRoman(num: int) -> str:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500,
                      'M': 1000}
    roman_numeral_list = list(reversed(roman_numerals.keys()))
    modulus_dict = {}
    remainder = num
    returning_str = ""

    for count, letter in enumerate(reversed(roman_numerals)):
        modulus_dict[letter], remainder = divmod(remainder, roman_numerals[letter])

        if modulus_dict[letter] < 4:
            for x in range(modulus_dict[letter]):
                returning_str += letter
        else:
            if modulus_dict[roman_numeral_list[count - 1]]:
                returning_str = returning_str[0:len(returning_str)-1] + letter + roman_numeral_list[count - 2]
            else:
                returning_str = returning_str[0:len(returning_str)] + letter + roman_numeral_list[count - 1]

    return returning_str


print(f"{intToRoman(999)}\t\t\tintToRoman(999)\nCMXCIX\t\t\t\tEXPECTED")
print(f"{intToRoman(3999)}\t\t\tintToRoman(3999)\nMMMCMXCIX\t\t\t\tEXPECTED")
print(f"{intToRoman(499)}\t\t\tintToRoman(499)\nCDXCIX\t\t\t\tEXPECTED")
