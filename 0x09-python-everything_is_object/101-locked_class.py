#!/usr/bin/python3
""" Locked class definition"""


class LockedClass:
    """
    prevents the user from dyn creating new instance attributes
    except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
