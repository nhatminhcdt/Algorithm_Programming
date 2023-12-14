from time import perf_counter
import pandas as pd
# Import local
import sys, os
sys.path.append(os.getcwd())
from helper_functions import utils

NUM_TEST_ELEMENTS = 10**6


def linear_seach(A, K):
  """Search for K in A
  @note This is a linear search algorithm.
  - Time complexity: O(n)
  - Space complexity: O(1) 

  Parameters
  ----------
  A : list, array...
      array to search
  K : value
      value to search for

  Returns
  -------
  int
      index of K in A, -1 if not found
  """
  for i in range(len(A)):
    if A[i] == K:
      return i
  return -1


def sentinel_search(A, K):
  """Search for K in A
  @note This is a sentinel search algorithm.
  - Time complexity: O(n)
  - Space complexity: O(1) 

  Parameters
  ----------
  A : list, array...
      array to search
  K : value
      value to search for

  Returns
  -------
  int
      index of K in A, -1 if not found
  """
  # Add sentinel
  A.append(K)
  i = 0
  while A[i] != K:
    i += 1
  # Remove sentinel
  A.pop()
  if i < len(A) or A[-1] == K:
    return i
  return -1


def jump_search(A, K):
  """Search for K in A
  @note This is a jump search algorithm.
  - Time complexity: O(sqrt(n))
  - Space complexity: O(1)
  @remark This algorithm is suitable for sorted array.

  Parameters
  ----------
  A : list, array...
      array to search
  K : value
      value to search for

  Returns
  -------
  int
      index of K in A, -1 if not found
  """
  n = len(A)
  step = int(n**0.5)
  i = 0
  while i < n:
    if A[i] == K:
      return i
    elif A[i] > K:
      break
    i += step
  # Linear search
  for j in range(i-step, i):
    if A[j] == K:
      return j
  return -1


def bin_search(A, K):
  """Search for K in A
  @note This is a binary search algorithm.
  - Time complexity: O(log(n))
  - Space complexity: O(1)
  @remark This algorithm is suitable for sorted array.

  Parameters
  ----------
  A : list, array...
      array to search
  K : value
      value to search for

  Returns
  -------
  int
      index of K in A, -1 if not found
  """
  left = 0
  right = len(A) - 1
  while left <= right:
    mid = (left + right) // 2
    if A[mid] == K:
      return mid
    elif A[mid] < K:
      left = mid + 1
    else:
      right = mid - 1
  return -1


"""@brief Implement test functions to test the above functions
"""

if __name__ == "__main__":
  func_lst = [linear_seach, sentinel_search, jump_search, bin_search]
  test_results = [utils.test_search_func(func, NUM_TEST_ELEMENTS) for func in func_lst]
  test_results_df = pd.DataFrame(pd.DataFrame(test_results, columns=["Algorithm", "Execution time (s)"]))
  print(test_results_df)
  print("==Algorithm with the best execution time:==")
  print(test_results_df.loc[test_results_df["Execution time (s)"] == test_results_df["Execution time (s)"].min()])
