# Assignment 4 for CSC401 Python

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
def function_two(perfect_number)

    return perfect_number

# Function Three(integer)
# Take an integer and return Perfect numbers <= number

# Function Four(list of mixed types)
# Take list of mixed type and count number of integers

# Function Five(list of anything)
# Take list of anything and remove second item

# ClassCircle
# Write class called circle, with an instance variable, for the radius
# and methods to calculate the area and circumference of the circle.


def main():
    print(function_one(['good', 'cat', 'bad', 'cat']))


if __name__ == "__main__":
    main()
