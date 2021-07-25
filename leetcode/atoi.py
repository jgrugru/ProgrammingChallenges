from re import search


def clamp_range(x):
    max_neg = -2 ** 31
    max_pos = 2 ** 31 - 1
    if x <= max_neg:
        return max_neg
    elif x >= max_pos:
        return max_pos
    else:
        return x


def find_digits_in_str(s: str):
    if search("(\-\-\W*\d+)|(\-\+\W*\d+)|(\+\+\W*\d+)|(\+\-\W*\d+)", s):
        return False
    else:
        return search("([-, +]*\d+)", s)


def contains_non_whitespace(s: str):
    return bool(search("\w|\.", s))


def leading_str_has_non_whitespace(s, r_index):
    return contains_non_whitespace(s[:r_index])


def whitespace_after_sign(s):
    match_object = search("((\-|\+)\W+\d+)", s)
    return bool(match_object)


def myAtoi(s: str) -> int:
    match_object = find_digits_in_str(s)

    if match_object:
        matched_number = match_object.group(0)
        if not leading_str_has_non_whitespace(s, match_object.span()[0]):
            digit_str = match_object.group(0)
            if whitespace_after_sign(digit_str):
                return 0

            x = int(matched_number)
            return clamp_range(x)

    return 0


print(myAtoi("    -12344"))
print(myAtoi("-91283472332"))
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("     "))
print(myAtoi("     ...   sdff  3"))
print(myAtoi("+-12"))
print(myAtoi("  -0012a42"))
print(myAtoi("  +  413"))

# flake8: noqa