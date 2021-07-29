def longestCommonPrefix(strs) -> str:
    shortest_str = min(strs, key=len)

    if len(strs) > 1:
        for s in strs:
            if shortest_str != s:
                index = len(shortest_str)
                while shortest_str[:index] != s[:index]:
                    index -= 1
                shortest_str = shortest_str[:index]

    return shortest_str


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["flow", "flow", "flow"]))
