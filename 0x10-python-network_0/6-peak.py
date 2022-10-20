#!/bin/bash/python3
""" a function of peak"""


def find_peak(list_of_integers):
    """find a peak in a list of unsorted orders """
    li = list_of_integers
    l1 = len(li)
    if l1 == 0:
        return
    p = l1 // 2
    if (p == l1 - 1 or li[p] >= li[p + 1] and p == 0 or li[p] >= li[p - 1]):
        return li[p]
    if p != l1 - 1 and li[p + 1] > li[p]:
        return find_peak(li[p + 1:])
    return find_peak(li[:p])
