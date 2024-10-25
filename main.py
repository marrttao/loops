import random


def generate_question(a_min, a_max, b_min, b_max):
    a = random.randint(a_min, a_max)
    b = random.randint(b_min, b_max)
    print(f"{a} * {b} = ")
    answer = int(input())
    return answer == a * b


def get_level(name, num_questions, a_min, a_max, b_min=1, b_max=10):
    correct_answers = 0
    print(name)
    for i in range(num_questions):
        if generate_question(a_min, a_max, b_min, b_max):
            correct_answers += 1
    return correct_answers


def calculate_grade(correct_answers):
    if correct_answers <= 5:
        print("Your mark is bad")
    elif correct_answers >= 9:
        print("Your mark is middle")
    else:
        print("Your mark is good")


def knowledge_of_multiplication_table():
    correct_answers = 0
    correct_answers += get_level("Easy level", 2, 1, 3)
    correct_answers += get_level("Middle level", 4, 4, 6)
    correct_answers += get_level("Hard level", 6, 7, 10)

    calculate_grade(correct_answers)


if __name__ == '__main__':
    knowledge_of_multiplication_table()
