def ranged_multiplication_table(start, end):
    result = []
    for i in range(start, end + 1):
        row = []
        for j in range(1, 10+1):
            print(f"{i} * {j} = {i * j}", end = " ")
        print("\n")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    ranged_multiplication_table(a, b)

