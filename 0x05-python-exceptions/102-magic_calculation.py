#!/usr/bin/python3
def f(a, b):
    result = 0
    for i in range(3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) // i
        except Exception:
            result += a + b
    return result


a = 3
b = 2

print(f(a, b))
