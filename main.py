def number_of_digits(number):
    int_number = int(number)
    digits_count = 0
    if int_number == 0:
        digits_count = 1
    else:
        while int_number > 0:
            int_number //= 10
            digits_count += 1
    print(f"number of digits: {digits_count}")

def number_of_zero(number):
    float_number = float(number)

    while number > 9:
        float_number /= 10
        number = int(float_number)

    zero_count = 0
    fractional_part = float_number - number


    while fractional_part != 0 and fractional_part * 10 < 1:
        fractional_part *= 10
        zero_count += 1

    print(f"Number of zeros: {zero_count}")



if __name__ == '__main__':
    number_of_zero(2567)

