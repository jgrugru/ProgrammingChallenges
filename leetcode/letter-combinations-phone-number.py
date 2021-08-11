from itertools import combinations, permutations
letter_map = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}


def letterCombinations(digits: str):
    combinations_list = []
    for digit in digits:
        combinations_list = combinations_list + letter_map[int(digit)]

    starting_combinations = permutations(combinations_list[0], r=len(digits))
    # for comb in combinations_list:

    return list(starting_combinations)
    # return list(combinations(combinations_list, r = len(digits)))


print(letterCombinations("23"))
