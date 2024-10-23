def multiplication_table(start, end):
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            print(f"{i} * {j} = {i * j}", end = " ")
        print("\n")

if __name__ == '__main__':
    multiplication_table(1, 10)
