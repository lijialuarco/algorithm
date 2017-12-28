def sum(numbers):
    print(type(numbers))
    if type(numbers) is int:
        numbers = [numbers]
    n = len(numbers)
    print(n)
    if n == 1:
        return numbers[0]
    else:
        return numbers.pop() + sum(numbers)


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    try:
        data = [int(item) for item in user_input.split(',')]
    except ValueError:
        print('para error')
    else:
        print(sum(data))
