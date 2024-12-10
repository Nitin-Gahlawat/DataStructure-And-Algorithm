from Sorting.Bin_sort import bin_sort
from Sorting.Bubble_sort import Bubble_sort
from Sorting.Count_sort import count_sort
from Sorting.Insertion_sort import Insertion_sort
from Sorting.Mearging import itrative_merge_sort, rec_merger_sort
from Sorting.Quick_sort import quick_sort
from Sorting.Selection_sort import selection_sort
from Sorting.Shell_short import shellsort
from Sorting.Radix_sort import radix_sort


def introduction():
    print("\nSorting")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Sorting ")
    print("example of Sorting algorithm")
    x = [4, 5, 16, 20, 10, 5, 6]
    print(f"Consider the array {x}")
    print(f"Array after Sort", selection_sort(x))
