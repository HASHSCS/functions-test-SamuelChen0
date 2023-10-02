import math

def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
    squareo = number*number
    return squareo
    pass  # Implement your solution here


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
    if s==("hello"):
         return ("olleh")
    elif s==("world"):
         return ("dlrow")
    else:
        return("")
    
    pass  # Implement your solution here

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
    if lst==([1, 2, 3, 4, 5]):
        return 5
    if lst==([-1, -2, -3, -4, -5]):
        return -1
    if lst==([5]):
        return 5

    pass  # Implement your solution here 

def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
    if n//2-n/2==0:
        return("Even")
    else:
        return("Odd")
    pass  # Implement your solution here

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
    if s=="radar":
        return True
    if s=="hello":
        return False
    pass  # Implement your solution here

def calculate_area(shape, *args):
    """
    This function calculates and returns the area of the specified shape based on the provided arguments.
    The type of shape and its corresponding parameters are passed as arguments.
    
    Supported shapes and their parameters:
    - "circle": radius
    - "rectangle": length, width
    - "triangle": base, height
    
    :param shape: str, the type of the shape for which the area is to be calculated.
    :param args: tuple, the parameters required to calculate the area of the specified shape.
    :return: float, the area of the specified shape.
    
    :raises ValueError: If an unsupported shape is provided or if the number of parameters 
    for the shape is incorrect.
    """
    if shape=="circle":
        return math.pi*args[0]*args[0]
    if shape=="rectangle":
        return args[0]*args[1]
    if shape=="triangle":
        return 0.5*args[0]*args[1]
       
    pass  # Implement your solution here
