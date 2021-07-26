from re import match


def isMatch(s: str, p: str) -> bool:
    p = "^" + p + "$"
    print(f"checking if {p} fits with {s}")
    match_object = match(p, s)

    return bool(match_object)


print(isMatch("aa", "a"))
print(isMatch("aa", "a*"))
print(isMatch("ab", ".*"))
print(isMatch("aab", "c*a*b*"))
print(isMatch("mississippi", "mis*is*p*."))
print(isMatch("aa", "a"))
print(isMatch("aa", "a"))
