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
    return search("([-,+]\d+$)|(\d+)", s)


def contains_non_whitespace(s: str):
    return bool(search("\w|.", s))


def leading_str_has_non_whitespace(s, r_index):
    return contains_non_whitespace(s[:r_index])


def myAtoi(s: str) -> int:
    match_object = find_digits_in_str(s)

    if match_object:
        if leading_str_has_non_whitespace(s, match_object.span()[0]):
            return 0
        else:
            x = int(match_object.group())
            return clamp_range(x)

    return match_object


print(myAtoi("    -12344"))
print(myAtoi("-91283472332"))
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("42"))
