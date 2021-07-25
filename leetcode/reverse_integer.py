def check_range(x):
    if x <= -2 ** 31 or x >= 2 ** 31 - 1:
        return 0
    else:
        return x


def reverse(x: int) -> int:
    is_negative = bool(x < 0)

    reverse_int = str(abs(x))

    if is_negative:
        return check_range(-1 * int(reverse_int[::-1]))
    else:
        return check_range(int(reverse_int[::-1]))


print(reverse(123450))
print(reverse(-123))
print(reverse(-12300))
print(reverse(120))
print(reverse(0))
print(reverse(-0))
print(reverse(-20000001000))
print(reverse(000000000000))
print(reverse(100000000))
print(reverse(1534236469))
print(2 ** 31 - 1)
