numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(number):
    return number % 2 == 0

filtered_numbers = list(filter(is_even, numbers))
