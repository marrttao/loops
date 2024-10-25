# main.py

def number_of_digits(number, test_mode=False):
    digits_count = 0
    if number == 0:
        digits_count = 1
    else:
        while number > 0:
            number //= 10
            digits_count += 1
    print(f"\n \nnumber of digits: {digits_count}\n")

    if not test_mode:
        choice_check(number)

    return digits_count


def number_of_zero(number, test_mode=False):

    count_of_zero = str(abs(number)).count('0')
    print(f"\n \nnumber of zero {count_of_zero}\n")

    if not test_mode:
        choice_check(number)

    return count_of_zero


def sum_of_number(number, test_mode=False):
    sum_digits = sum(int(digit) for digit in str(number))
    print(f"\n \nthe sum is {sum_digits}\n")

    if not test_mode:
        choice_check(number)

    return sum_digits


def middle_average(number, test_mode=False):
    digits = [int(digit) for digit in str(number)]
    average = int(sum(digits) / len(digits))
    print(f"\n \nmidle average {average}\n")

    if not test_mode:
        choice_check(number)

    return average


def menu():
    print(" ============= \n",
          "1 - number of digits \n",
          "------------- \n",
          "2 - number of zero's \n",
          "------------- \n",
          "3 - sum of number \n",
          "------------- \n",
          "4 - middle average of number \n",
          "============= \n",
          "0 - change the number")


def choice_check(number):
    menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        number_of_digits(number)
    elif choice == 2:
        number_of_zero(number)
    elif choice == 3:
        sum_of_number(number)
    elif choice == 4:
        middle_average(number)
    elif choice == 0:
        number = int(input("Write a number: "))
        choice_check(number)
    else:
        print("Invalid choice. Please try again.")
        choice_check(number)


if __name__ == '__main__':
    number = int(input("Write a number: "))
    choice_check(number)
