def rhombus(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))
    for i in range(size - 2, -1,-1):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))
if __name__ == '__main__':
    size = int(input("Write a size of rhombus "))
    rhombus(size)