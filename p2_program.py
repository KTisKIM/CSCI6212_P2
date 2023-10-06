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

# import heapq as heapify, heappop
import heapq
import time

# Finds the merge sequence, given an array
# that contains the sizes of the lists
def merge_sequence(nums_array):
    start = time.perf_counter_ns()      ### Start time ###

    # Build the original heap
    print('---previous heapify', nums_array)
    heapq.heapify(nums_array)
    print('---after heapify', nums_array)
    for i in range(1, len(nums_array)):
        # Remove two smallest elements from the heap - 2 log (n) time for two delete operations
        first_smallest = heapq.heappop(nums_array)
        second_smallest = heapq.heappop(nums_array)
        print("---first:", first_smallest, "second:", second_smallest)
        print('---after pop', nums_array)
        # Add a new element corresponding to the merged list - log(n) time for one insert operation
        heapq.heappush(nums_array, first_smallest + second_smallest)
        print('---after push', nums_array)

    end = time.perf_counter_ns()        ### End time ###

    print(f"{end - start} nanoseconds")  # Experimental result

    return nums_array


if __name__ == "__main__":
    n = #
    a = [4, 8, 1, 3, 5]  # array of numbers

    merge_sequence(a)
