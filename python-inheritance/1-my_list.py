#!/usr/bin/python3
This module defines a class that inherits from list
"""


class MyList(list):
     """
     This class takes the functionality inheriting from list.
     """

     def print_sorted(self):
         """
         This function prints a copy of the sorted list.
         """

         print(sorted(self))

     def __repr__(self):
         """
         This method returns a string, list representation.

         Returns:
             list (list): Returns the representation of the list.
         """

         return f"{list(self)}"
