#сделал возможность выбирать размер ромба при проверке увидите

def rhombus(len_1, len_2):
    print("\n")
    for i in range(len_1):
        for j in range(len_2):
            if j >= len_2 - i - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        for j in range(len_2):
            if j+1 <= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')

        print()

    for i in range(len_1 - 1, -1, -1):
        for j in range(len_2):
            if j-1 >= len_2 - i - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        for j in range(len_2):
            if j+2 <= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')

        print()


if __name__ == '__main__':
    len_1 = int(input("Write a len_1 of rhombus"))
    len_2 = int(input("Write a len_2 of rhombus"))
    rhombus(len_1, len_2)
