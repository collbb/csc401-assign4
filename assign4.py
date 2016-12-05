# Assignment 4 for CSC401 Python
import functools
from Circle import Circle

# Function One(list of strings)
# Take a list of strings as a parameter and return all unique strings
def function_one(string_list):
    unique_list = []
    unique = True
    for x in range(len(string_list)):
        string_test = string_list[x]
        for y in range(len(string_list)):
            if string_test == string_list[y] and x != y:
                unique = False
                break
            elif string_test != string_list[y]:
                unique = True

        if unique:
            unique_list.append(string_test)

    # set_list = list(set(string_list))
    return unique_list

# Function Two(integer)
# Take an integer and return whether or not the number is Perfect
# Perfect number = sum of divisors = number
def function_two(perfect_number):
    #    factors_list = []
    #    for i in range(1,perfect_number):
    #        if (perfect_number % i) == 0:
    #            factors_list.append(i)
    sum_of = sum(factors(perfect_number))-perfect_number
    if  sum_of == perfect_number and sum_of > 1:
        return True
    else:
        return False


# Function Three(integer)
# Take an integer and return Perfect numbers <= number
def function_three(perfect_number_two):
    list_of_pn = []
    for i in range(1,perfect_number_two):
        if function_two(i):
            list_of_pn.append(i)

    return list_of_pn


# Function Four(list of mixed types)
# Take list of mixed type and count number of integers
def function_four(mixed_list):
    count = 0
    for i in range(len(mixed_list)):
        if isinstance(mixed_list[i], int):
            count += 1
        elif isinstance(mixed_list[i],list):
            count += function_four(mixed_list[i])

    return count

# Function Five(list of anything)
# Take list of anything and remove second item
def function_five(list_of_anything = []):
    if len(list_of_anything) > 1:
        del list_of_anything[1]

    return list_of_anything


# ClassCircle
# Write class called circle, with an instance variable, for the radius
# and methods to calculate the area and circumference of the circle.

# Factors function borrowed from: http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
# Quicker than my for loop method
def factors(n):
    return functools.reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))

def main():
    print(function_one(['good', 'cat', 'bad', 'cat']))
    print(function_two(496))
    print(function_three(2048))
    print(function_four([1, ['A', 2], 'B', 3, 'C', 4, ['D', 5]]))
    print(function_five(['A', ['A', 'B'], 'C']))

    my_circle = Circle()
    my_circle.radius = 5

    print(my_circle.area())
    print(my_circle.circumference())



if __name__ == "__main__":
    main()


