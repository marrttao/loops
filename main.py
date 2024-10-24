def multiplication_table(start, end):
    result = []
    for i in range(start, end + 1):
        row = []
        for j in range(start, end + 1):
            row.append(f"{i} * {j} = {i * j}")
            print(f"{i} * {j} = {i * j}", end = " ")
            result.append(row)
        print("\n")
    return result

if __name__ == '__main__':

    multiplication_table(1, 10)
