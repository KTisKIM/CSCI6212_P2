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
        // (n) time for building the original heap
    For i = 1 to n-1
        Remove two smallest elements from the heap
            // 2 log(n) time for two delete operations
        Add a new element corresponding to the merged list
            // log(n) time for one insert operation
        Sum of the total cost and the size of the new merged list
"""

# import heapq
# import time
# import random
from heapq import heapify, heappop, heappush
from time import perf_counter_ns
from random import choice

# Finds the merge sequence, given an array
# that contains the sizes of the lists
def merge_sequence(nums_array):
    start = perf_counter_ns()           ### Start time ###

    total_cost = 0

    # Build the original heap - (n) time for building the original heap
    heapify(nums_array)
    for i in range(1, len(nums_array)):
        # Remove two smallest elements from the heap - 2 log(n) time for two delete operations
        first_smallest = heappop(nums_array)
        second_smallest = heappop(nums_array)
        # Add a new element corresponding to the merged list - log(n) time for one insert operation
        heappush(nums_array, first_smallest + second_smallest)

        # Sum of the total cost and the size of the new merged list
        total_cost += first_smallest + second_smallest

    end = perf_counter_ns()             ### End time ###
    print(f"Running time: {end - start} nanoseconds") ### Experimental result ###

    return nums_array, total_cost


if __name__ == "__main__":
    n = 500000                                      # size of the array
    zero_to_nine = list(range(10))                  # numbers between 0-9 for the input array.
    a = [choice(zero_to_nine) for i in range(n)]    # array of numbers based on the size of 'n'

    final_nums_array, final_total_cost = merge_sequence(a)
    print(f"Merged List: {final_nums_array} | Total Cost: {final_total_cost}")
