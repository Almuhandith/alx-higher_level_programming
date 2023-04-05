#!/usr/bin/python3
"""Algorithms for array of integers."""


def find_peak(array_of_integers):
    """Finds a peak in a array of unsorted integers."""
    if array_of_integers:
        array_of_integers.sort(reverse=True)
        return array_of_integers[0]
