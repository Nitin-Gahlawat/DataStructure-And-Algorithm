from __future__ import annotations

from Array.ArrayOprations import ArrayOprtations
from Array.DuplicateElement import count_elements_unsorted,duplicate_sorted,duplicate_sorted_meth2,duplicate_sorted_meth3,duplicate_unsorted
from Array.FindMinMax import find_min_max
from Array.MissingElement import missing_element_sorted_meth1,missing_element_sorted_meth2,missing_element_unsorted
from Array.Searching import Searching
from Array.SumPair import sum_pair,sum_pair_hash,sum_pair_sorted
from Array.SetOprations import SetOpration
from Array.ArrayClass import Array






def introduction():
    print("\nArray")
    print("-"*120)
    print("This Module Contation all the algorithm related to the Array datastructure")
    print("example of array algorithm")
    x=Array(1,2,3,4,5,6)
    y=Array(100,101,102,103,104)
    print(f"Consider two array {x} {y}")
    x.concat(y)
    print(f"Concation of the two are {x}")
