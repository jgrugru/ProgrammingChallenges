def maxArea(height):
    max_area = 0
    l_index = 0
    r_index = len(height) - 1

    while l_index < r_index:
        l, r = height[l_index], height[r_index]
        length = r_index - l_index
        width = min(l, r)
        max_area = max(max_area, length * width)

        if l > r:
            r_index -= 1
        else:
            l_index += 1

    return max_area


# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([0,0]))
# print(maxArea([0,1]))
# print(maxArea([0,0,0,0,0,0,1]))
# print(maxArea([10000,0,0,0,0,0,0,0,0,0,0,1]))
# print(maxArea([1,1]))
