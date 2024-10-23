def simple_number(a, b):
    for num in range(a, b + 1):
        is_simple = True
        for j in range(2, num):
            if num % j == 0:
                is_simple = False
                break
        if is_simple and num > 1:
            print(num)
if __name__ == '__main__':

    a = int(input())
    b = int(input())
    simple_number(a,b)