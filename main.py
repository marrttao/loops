def ranged_multiplication_table(start, end):
    for i in range(start, end + 1):
        for j in range(start, 10+1):
            print(f"{i} * {j} = {i * j}", end = " ")
        print("\n")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    ranged_multiplication_table(a, b)

