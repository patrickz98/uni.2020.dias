# -*- coding: utf-8 -*-


# Write a function that returns the sum of squares of two variables.
def sum_of_squares(var1: int, var2: int) -> int:
    return (var1 ** 2) + (var2 ** 2)


# Write a function that increments the value of a variable by 1.
def increments_value(var: int) -> int:
    return var + 1


# Write a function that increments the value of a variable by a number n.
def increments_value_by_number(var: int, num: int) -> int:
    return var + num


# Write a function that calculates the factorial of a number (n!).
def factorial(var: int) -> int:
    num = 1

    if var < 0:
        # See https://en.wikipedia.org/wiki/Factorial for details
        return 1

    for x in range(1, var):
        num *= x

    return num


# Use the 'for' and the 'while' statement to display numbers between 1 and 10.
def display_useless_numbers():
    for num in range(1, 101):
        print(num)

    inx = 1
    while inx < 101:
        print(inx)
        inx += 1


# Write a function that checks whether a number is between 1 and 10.
def check_number_is_between_1_10(num: int) -> bool:
    return (num > 1) and (num < 10)


# Write a function that checks for two numbers the following conditions
def check_conditions(x: int, y: int):
    if x < y:
        print(x, "<", y)

    if x > y:
        print(x, ">", y)

    if x == y:
        print(x, "==", y)


# Write a function that checks whether a number is prime or not.
def is_prime(var: int) -> bool:

    if var <= 1:
        return False

    for i in range(2, var):
        if (var % i) == 0:
            return False

    return True


def main():
    print("hello world!")
    display_useless_numbers()
    print(is_prime(13))
    print(is_prime(20))
    print(is_prime(27))


if __name__ == "__main__":
    main()
