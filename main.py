def chess_desk(large_of_square):
    if large_of_square <= 0:

        for _ in range(6):
            print(" ")
        return
    rows = 6
    columns = 8
    for i in range(rows):
        for j in range(columns // 2):
            print('*' * large_of_square, end=' ')
            print('-' * large_of_square, end=' ')
        print()
if __name__ == '__main__':
    size = int(input())
    chess_desk(size)