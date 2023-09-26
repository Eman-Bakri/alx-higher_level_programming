#!/usr/bin/python3
"""Definition of Square class."""


class Square:
    """Square representation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return Square area."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define equal == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define not equal != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define less than < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define less or equal <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define greater than > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define greater or equal >= compmarison to a Square."""
        return self.area() >= other.area()
