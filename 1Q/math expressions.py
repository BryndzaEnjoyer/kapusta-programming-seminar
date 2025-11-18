# ============================================
# 1. Basic Arithmetic Functions
# ============================================

def subtract(a, b):
    """
    Subtracts one number from another.

    Parameters
    ----------
    a : float or int
        The number to subtract from.
    b : float or int
        The number to subtract.

    Returns
    -------
    result : float or int
        The result of a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    product : float or int
        The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divides one number by another.

    Parameters
    ----------
    a : float or int
        The dividend.
    b : float or int
        The divisor (cannot be zero).

    Returns
    -------
    quotient : float
        The result of a / b.

    Raises
    ------
    ZeroDivisionError
        If b is equal to zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def floor_divide(a, b):
    """
    Performs floor division between two numbers.

    Parameters
    ----------
    a : float or int
        The dividend.
    b : float or int
        The divisor.

    Returns
    -------
    result : int
        The result of a // b.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a // b


def modulus(a, b):
    """
    Returns the remainder of division between two numbers.

    Parameters
    ----------
    a : float or int
        The dividend.
    b : float or int
        The divisor.

    Returns
    -------
    remainder : int or float
        The remainder of a % b.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a % b


def power(a, b):
    """
    Raises a number to a power.

    Parameters
    ----------
    a : float or int
        The base number.
    b : float or int
        The exponent.

    Returns
    -------
    result : float or int
        The value of a raised to the power of b.
    """
    return a ** b


# Tests
print("Section 1 Tests:")
print(subtract(10, 4))
print(multiply(3, 5))
print(divide(10, 2))
print(floor_divide(10, 3))
print(modulus(10, 3))
print(power(2, 3))
print()


# ============================================
# 2. Combining Operators
# ============================================

def add(a, b):
    """
    Adds two numbers.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    total : float or int
        The sum of a and b.
    """
    return a + b


def average(a, b):
    """
    Calculates the average of two numbers.

    Parameters
    ----------
    a : float or int
        The first number.
    b : float or int
        The second number.

    Returns
    -------
    average_value : float
        The average of a and b.
    """
    return divide(add(a, b), 2)


def area_rectangle(length, width):
    """
    Calculates the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle.
    width : float or int
        The width of the rectangle.

    Returns
    -------
    area : float or int
        The area of the rectangle.
    """
    return multiply(length, width)


def perimeter_rectangle(length, width):
    """
    Calculates the perimeter of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle.
    width : float or int
        The width of the rectangle.

    Returns
    -------
    perimeter : float or int
        The perimeter of the rectangle.
    """
    return multiply(2, add(length, width))


# Tests
print("Section 2 Tests:")
print(average(4, 6))
print(area_rectangle(4, 5))
print(perimeter_rectangle(4, 5))
print()


# ============================================
# 3. More Complex Formulas
# ============================================

def area_triangle(base, height):
    """
    Calculates the area of a triangle.

    Parameters
    ----------
    base : float or int
        The base of the triangle.
    height : float or int
        The height of the triangle.

    Returns
    -------
    area : float
        The area of the triangle.
    """
    return divide(multiply(base, height), 2)


def pythagoras(a, b):
    """
    Applies the Pythagorean theorem to find the hypotenuse of a right triangle.

    Parameters
    ----------
    a : float or int
        Length of one leg.
    b : float or int
        Length of the other leg.

    Returns
    -------
    c : float
        Length of the hypotenuse.
    """
    return power(add(power(a, 2), power(b, 2)), 0.5)


def quadratic_roots(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters
    ----------
    a : float
        Coefficient of x^2.
    b : float
        Coefficient of x.
    c : float
        Constant term.

    Returns
    -------
    roots : tuple
        A tuple (root1, root2) containing the two real roots.
        Returns (None, None) if there are no real roots.
    """
    discriminant = power(b, 2) - 4 * a * c
    if discriminant < 0:
        return None, None
    sqrt_d = power(discriminant, 0.5)
    root1 = divide(-b + sqrt_d, 2 * a)
    root2 = divide(-b - sqrt_d, 2 * a)
    return root1, root2


# Tests
print("Section 3 Tests:")
print(area_triangle(4, 6))
print(pythagoras(3, 4))
print(quadratic_roots(1, -3, 2))
print()


# ============================================
# 4. Challenge Exercises
# ============================================

def distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points in a 2D plane.

    Parameters
    ----------
    x1 : float
        X-coordinate of the first point.
    y1 : float
        Y-coordinate of the first point.
    x2 : float
        X-coordinate of the second point.
    y2 : float
        Y-coordinate of the second point.

    Returns
    -------
    distance : float
        The distance between the two points.
    """
    return power(power(x2 - x1, 2) + power(y2 - y1, 2), 0.5)


def bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI).

    Parameters
    ----------
    weight : float
        Weight in kilograms.
    height : float
        Height in meters.

    Returns
    -------
    bmi_value : float
        The calculated BMI.
    """
    return divide(weight, power(height, 2))


def celsius_to_fahrenheit(c):
    """
    Converts temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    c : float
        Temperature in Celsius.

    Returns
    -------
    f : float
        Temperature in Fahrenheit.
    """
    return (c * 9/5) + 32


# Tests
print("Section 4 Tests:")
print(distance(0, 0, 3, 4))
print(bmi(70, 1.75))
print(celsius_to_fahrenheit(0))
print()

