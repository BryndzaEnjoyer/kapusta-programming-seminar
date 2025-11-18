def task1():
    """
    Check the temperature value and print a message describing the weather.

    How it works:
        - Sets a temperature value (currently fixed at 30°C).
        - If the temperature is above 25°C, it prints: "It's warm outside!".
        - Otherwise, it prints: "It's cool."

    Parameters:
        None

    Returns:
        None
    """
    temperature = 30
    if temperature > 25:
        print("It's warm outside!")
    else:
        print("It's cool.")

def task2():
    """
    Ask the user for a number and display a message based on whether it is
    positive, negative, or zero.

    How it works:
        - Reads an integer from user input.
        - Checks if the number is > 0, < 0, or == 0.
        - Prints a message based on the category.

    Parameters:
        None

    Returns:
        None
    """
    n1 = int(input("first number: "))
    if n1 > 0:
        print("boring")
    elif n1 < 0:
        print("still not interested")
    elif n1 == 0:
        print("are you sure?")


def task3():
    """
    Ask the user for two numbers and check if they are both even,
    both odd, or mixed.

    How it works:
        - Reads two integers from input.
        - Uses the modulus operator % to check even/odd.
        - Prints an appropriate message.

    Parameters:
        None

    Returns:
        None
    """
    n1 = int(input("first number: "))
    n2 = int(input("second number: "))
    if n1 % 2 == 0 and n2 % 2 == 0:
        print("Both even")
    elif n1 % 2 == 1 and n2 % 2 == 1:
        print("You are weird")
    else:
        print("not one like the other")


def task4():
    """
    Check if a password is valid based on two conditions:
        - It contains the word 'python'
        - Its length is greater than 7

    Parameters:
        None

    Returns:
        None
    """
    pas = input("enter password: ")
    if "python" in pas and len(pas) > 7:
        print("ok")
    else:
        print("not ok")


def task5():
    """
    Act like a traffic light interpreter.
    Ask the user for a color and print the appropriate instruction.

    Accepted inputs (case-insensitive):
        - 'red' → 'stop'
        - 'yellow' → 'Slow down'
        - 'green' → 'go'

    Parameters:
        None

    Returns:
        None
    """
    color = input("enter red, yellow or green: ")
    if color.lower() == "red":
        print("stop")
    elif color.lower() == "yellow":
        print("Slow down")
    elif color.lower() == "green":
        print("go")
    else:
        print("wrong input")


def task6():
    """
    Check if a person is allowed to enter based on age and ticket.

    Conditions:
        - User must be older than 11
        - User must have a ticket ('yes')

    Fix included:
        - Converts age to int because input() returns a string
        - Uses correct comparison ticket.lower() == "yes"

    Parameters:
        None

    Returns:
        None
    """
    age = int(input("Enter your AGE! "))
    ticket = input("DO YOU HAVE A TICKET! ")

    if age > 11 and ticket.lower() == "yes":
        print("Enter!")
    else:
        print("You shall not pass!")


def is_triangle8(a, b, c):
    """
    Determine whether three side lengths can form a triangle.

    How it works:
        - Puts sides into a list
        - Partially sorts list so the largest number is last
        - Uses triangle inequality:
            largest < sum of the other two → triangle is possible

    Parameters:
        a, b, c : int
            Side lengths of the triangle.

    Returns:
        str : 'is possible' or 'is degenerate'
    """
    l = [a, b, c]
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

    print(l)

    if l[-1] < l[0] + l[1]:
        return "is possible"
    else:
        return "is degenerate"


def task8():
    """
    Ask the user for three side lengths and determine whether a triangle
    can be formed using the triangle inequality rule.

    How it works:
        - Reads 3 integers from input.
        - Passes them to is_triangle8().
        - Prints the result.

    Parameters:
        None

    Returns:
        None
    """
    print("Enter triangle's side lengths:")
    a = int(input("a "))
    b = int(input("b "))
    c = int(input("c "))
    print(f"The triangle {is_triangle8(a, b, c)}")


# Run task8 by default
task8()
