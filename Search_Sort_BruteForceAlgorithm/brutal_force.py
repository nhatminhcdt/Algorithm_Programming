from time import perf_counter
from random import randint

# Import local
import sys, os
sys.path.append(os.getcwd())
from helper_functions import utils

NUM_TEST_ELEMENTS = 10**4


def natural_sort(A):
  """@brief Sort array A using natural sort algorithm
  @note This is a natural sort algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to sort
  """
  n = len(A)
  for i in range(n-1):
    for j in range(i+1, n):
      if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]


def exp(a:int, n:int):
  """@brief Compute a^n
  @note This is a exponential function.
  - Time complexity: O(n)
  - Space complexity: O(1)
  @param a : int
      base
  @param n : int
      exponent
  @return int
      a^n
  """
  p = 1
  for i in range(1, n+1):
    p *= a
  return p


def dist(p, q):
  """@brief Compute the distance between p and q
  @param p : int
      point p
  @param q : int
      point q
  @return int
      distance between p and q
  """
  from math import sqrt
  return sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


def closet_pair_1(P):
  """@brief Find the closet pair in P
  @note This is a closet pair algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to search
  @return int
      index of the closet pair in A
  """
  n = len(P)
  min_dist = float('inf')
  for i in range(n-1):
    for j in range(i+1, n):
      dist_ = dist(P[i], P[j])
      if min_dist > dist_:
        min_dist = dist_
        index = [i, j]
  return [index, min_dist]


def closet_pair_2(P):
  """@brief Find the closet pair in P
  @note This is a closet pair algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to search
  @return int
      index of the closet pair in A
  """
  n = len(P)
  p = P[0]
  q = P[1]
  min_dist = dist(p, q)
  for i in range(n-1):
    for j in range(i+1, n):
      dist_ = dist(P[i], P[j])
      if min_dist > dist_:
        min_dist = dist_
        index = [i, j]
  return [index, min_dist]


def cal_sum(A, i, j):
  """@brief Compute the sum of elements in A[i:j+1]
  @param A : list, array...
      array to search
  @param i : int
      start index
  @param j : int
      end index
  @return int
      sum of elements in A[i:j+1]
  """
  sum_ = 0
  for k in range(i, j+1):
    sum_ += A[k]
  return sum_


def max_subarray_1(A):
  """@brief Find the max subarray in A
  @example: A = [1, -3, 2, 1, -1] => max_subarray = [2, 1]
  @note This is a max subarray algorithm.
  - Time complexity: O(n^3)
  - Space complexity: O(1)
  @param A : list, array...
      array to search
  @return [[int, int], int]
      index of the max subarray in A and its sum
  """
  n = len(A)
  max_sum = float('-inf')
  for i in range(n):
    for j in range(i, n):
      sum_ = cal_sum(A, i, j)
      if max_sum < sum_:
        max_sum = sum_
        boundary = [i, j]
  return [boundary, max_sum]


def max_subarray_2(A):
  """@brief Find the max subarray in A
  @example: A = [1, -3, 2, 1, -1] => max_subarray = [2, 1]
  @note This is a max subarray algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to search
  @return [[int, int], int]
      index of the max subarray in A and its sum
  """
  n = len(A)
  max_sum = A[0]
  for i in range(n):
    sum_ = 0
    for j in range(i, n):
      sum_ += A[j]
      if max_sum < sum_:
        max_sum = sum_
        boundary = [i, j]
  return [boundary, max_sum]


def maxlength_subarray(A):
  """@brief Find the max length subarray in A
  @example: A = [1, 2, 3, 2, 1, 4, 5, 9] => max_subarray = [1, 4, 5, 9]
  @note This is a max length subarray algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  @param A : list, array...
      array to search
  @return [int, int]
      index of the max length subarray in A and its length
  """
  n = len(A)
  i_max = 0
  max_len = 1
  for i in range(n):
    j = i
    length = 1
    while j < n-1 and A[j] < A[j+1]:
      j += 1
      length += 1
    if max_len < length:
      max_len = length
      i_max = i
  return [i_max, max_len]


"""Implement test function to test the above functions
"""
def test_closet_pair(alg_func, n:int):
  """@brief Implement test function for closet pair algorithm
  @param alg_func : function
      algorithm function
  @param n : int
      size of array
  """
  # Get function name
  func_name = alg_func.__name__
  # Create random array, with each element is a point in 2D, do not repeat
  P = []
  while len(P) < n:
    p = [randint(0, n), randint(0, n)]
    if p not in P:
      P.append(p)
  # Test closet_pair
  start = perf_counter()
  index, min_val = closet_pair_1(P)
  exec_time = round(perf_counter() - start, 2)
  # Print results
  print(f"{func_name}: {exec_time}(s), \n\tindex = {index}, points: [{P[index[0]]}, {P[index[1]]}], min_val = {min_val}")
  return [func_name, exec_time]


if __name__ == "__main__":
  # Test natural_sort
  utils.test_sort_func(natural_sort, NUM_TEST_ELEMENTS)
  print("\n")
  # Test exp
  utils.test_alg_func(exp, 2, 10**5)
  print("\n")
  # Test closet_pair_1
  test_closet_pair(closet_pair_1, 10**3)
  # Test closet_pair_2
  test_closet_pair(closet_pair_2, 10**3)
  print("\n")
  # Test max_subarray_1
  A = utils.create_array(10**3)
  _,_,ret = utils.test_alg_func(max_subarray_1, A)
  print(f"boundary = {ret[0]}, max_sum = {ret[1]}")
  # Test max_subarray_2
  A = utils.create_array(10**3)
  _,_,ret = utils.test_alg_func(max_subarray_2, A)
  print(f"boundary = {ret[0]}, max_sum = {ret[1]}")
  print("\n")
  # Test maxlength_subarray
  A = utils.create_array(10**4)
  _,_,ret = utils.test_alg_func(maxlength_subarray, A)
  print(f"i_max = {ret[0]}, max_length = {ret[1]}")
