#!/usr/bin/env python3
"""
This module contains a type-annotated function sum_list
that takes a list input_list of floats as an argument
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]):
    """
    Return the sum of the floats in the given list.
    """
    return sum(input_list)
