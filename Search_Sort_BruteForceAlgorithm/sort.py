from time import perf_counter
from random import randint
import pandas as pd

# Import local
import sys, os
sys.path.append(os.getcwd())
from helper_functions import utils

NUM_TEST_ELEMENTS = 10**4


def insert_sort_1(A):
  """@brief Sort array A using insertion sort algorithm
  @note This is a insertion sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to sort
  """
  for i in range (1, len(A)):
    j = i
    while j > 0 and A[j] < A[j-1]:
      A[j], A[j-1] = A[j-1], A[j]
      j -= 1


def insert_sort_2(A):
  """@brief Sort array A using insertion sort algorithm
  @note This is a insertion sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to sort
  """
  for i in range (1, len(A)):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key


def insert_sort_3(A):
  """@brief Sort array A using insertion sort algorithm
  @note This is a insertion sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to sort
  """
  for i in range (1, len(A)):
    key = A[i]
    j = i
    while j > 0 and A[j-1] > key:
      A[j] = A[j-1]
      j -= 1
    A[j] = key


def selection_sort(A):
  """@brief Sort array A using selection sort algorithm
  @note This is a selection sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to sort
  """
  n = len(A)
  for i in range(n-1):
    min_idx = i
    for j in range(i, n):
      if A[j] < A[min_idx]:
        min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]


def bubble_sort_1(A):
  """@brief Sort array A using bubble sort algorithm
  @note This is a bubble sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array..
      array to sort
  """
  n = len(A)
  for i in range(n-1):
    for j in range(n-1-i):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]


def bubble_sort_2(A):
  """@brief Sort array A using bubble sort algorithm
  @note This is a bubble sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array..
      array to sort
  """
  n = len(A)
  for i in range(n-2, -1, -1):
    for j in range(i+1):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]


def bubble_sort_3(A):
  """@brief Sort array A using bubble sort algorithm
  @note This is a bubble sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array..
      array to sort
  """
  n = len(A)
  for i in range(1, n):
    for j in range(n-1, i-1, -1):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]


if __name__ == "__main__":
  test_funcs = [insert_sort_1,
                insert_sort_2,
                insert_sort_3,
                selection_sort,
                bubble_sort_1,
                bubble_sort_2,
                bubble_sort_3,
                ]
  test_results_df = pd.DataFrame(columns=["Algorithm", "Execution time (s)"])
  for test_func in test_funcs:
    result = utils.test_sort_func(test_func, NUM_TEST_ELEMENTS)
    print(result)
    test_results_df.loc[len(test_results_df)] = result
    print("\n")
  print(test_results_df)
  # Print the algorithm with the best execution time
  print("\n")
  print("Algorithm with the best execution time: ")
  print(test_results_df[test_results_df["Execution time (s)"] == test_results_df["Execution time (s)"].min()])