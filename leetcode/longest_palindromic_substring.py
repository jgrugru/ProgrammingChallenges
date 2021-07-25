def is_palindrome(s):
    return s == s[::-1]


def longestPalindrome(s: str) -> str:
    largest_palindrome = s[0]
    # l_index = 0
    r_index = len(s) - 1

    for l_index in range(len(s)):
        r_index = len(s) - 1
        while (r_index - l_index) >= len(largest_palindrome):
            # breakpoint()

            if l_index == r_index:
                break
            elif s[l_index] == s[r_index]:
                test_str = s[l_index:r_index+1]
                if is_palindrome(test_str):
                    if len(largest_palindrome) < len(test_str):
                        largest_palindrome = test_str
                        break
                else:
                    r_index -= 1
            else:
                r_index -= 1

    return largest_palindrome


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))
print(longestPalindrome("fffjabbba"))
print(longestPalindrome("dakkjkqekafklhadfddaa"))
print(longestPalindrome("bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
#
