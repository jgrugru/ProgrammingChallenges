def romanToInt(s: str) -> int:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    returning_value = 0
    skip_value = False

    for count, numeral in enumerate(s):
        if not skip_value:
            returning_value += roman_numerals[numeral]
        else:
            skip_value = False
        if count + 1 < len(s):
            if roman_numerals[s[count+1]] > roman_numerals[numeral]:
                returning_value += roman_numerals[s[count+1]] - (roman_numerals[numeral] * 2)
                skip_value = True

    return returning_value


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("MCMXCIV"))
print(romanToInt("CDXCIX"))
print(romanToInt("XL"))
print(romanToInt("XC"))
print(romanToInt("LXXXIX"))
