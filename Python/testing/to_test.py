def floor_div(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError
    return a // b

if __name__ == '__main__':
    print(floor_div(-3,3))