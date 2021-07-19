def lengthOfLongestSubstring(s: str) -> int:
    """
    l_index represents the left index. It adds one, shrinking the window
    as soon as a duplicate is found and keeps shrinking until
    the duplicate no longer appears in the window. r_index represents
    the right index.
    """
    charSet = set()
    result = 0
    l_index = 0

    for r_index in range(len(s)):
        while s[r_index] in charSet:
            charSet.remove(s[l_index])
            r_index += 1
        charSet.add(s[r_index])
        result = max(result, r_index - l_index + 1)

    return result


print(lengthOfLongestSubstring("abc"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbbb"))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("pwwwkew"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("anviaj"))
print(lengthOfLongestSubstring("plmaiaj"))
print(lengthOfLongestSubstring(""))
