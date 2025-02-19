def meow(n: int) -> str:
    """
    Meow n Times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A String of n meows, one per line
    :rtype: str
    """
    return "Meow\n" * n

number: int = int(input("Number: "))
meows: str =meow(number)
print(meows, end="")



