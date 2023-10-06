#################################
#   Name: Keuntae Kim           #
#   GWID: G30341718             #
#   Course: CSIC 6212 - 12      #
#   Professor: Amrinder Arora   #
#        < Project 2 >          #
#################################

"""
// Finds the merge sequence, given an array
// that contains the sizes of the lists
Algorithm MergeSequence (Input: Array L[1..n], L[i] is the size of the i-th list)
    Build the original heap
    For i = 1 to n-1
        Remove two smallest elements from the heap
            // 2 log (n) time for two delete operations
        Add a new element corresponding to the merged list
            // log(n) time for one insert operation
"""

# import heapq
from heapq import heapify, heappop, heappush
# import time
from time import perf_counter_ns
# import random
from random import choice

# Finds the merge sequence, given an array
# that contains the sizes of the lists
def merge_sequence(nums_array):
    start = perf_counter_ns()      ### Start time ###

    total_cost = 0

    print("-----BEFORE heapify", nums_array)
    # Build the original heap
    heapify(nums_array)
    print("-----AFTER heapify", nums_array)
    for i in range(1, len(nums_array)):
        # Remove two smallest elements from the heap - 2 log (n) time for two delete operations
        first_smallest = heappop(nums_array)
        second_smallest = heappop(nums_array)
        print("-----FIRST:", first_smallest, "SECOND:", second_smallest)
        print("-----AFTER popping", nums_array)
        # Add a new element corresponding to the merged list - log(n) time for one insert operation
        heappush(nums_array, first_smallest + second_smallest)
        print('-----AFTER push', nums_array)

        total_cost += first_smallest + second_smallest  # Total cost of merging all the lists

    end = perf_counter_ns()        ### End time ###
    print(f"Total Cost: {total_cost}")
    print(f"{end - start} nanoseconds") ### Experimental result ###

    return nums_array, total_cost


if __name__ == "__main__":
    n = 10  # need to define 'n'
    zero_to_nine = list(range(10))
    a = [choice(zero_to_nine) for i in range(n)]    # array of numbers

    final_nums_array, final_total_cost = merge_sequence(a)
    print("\n최종 답", final_nums_array, final_total_cost)
