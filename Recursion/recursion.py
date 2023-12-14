"""Contains functions that use recursion algorithm.

@todo Add test cases for polynomial_fast_calc, hanoi function
"""

import random
from math import gcd
import pandas as pd
# Import local
import sys, os
sys.path.append(os.getcwd())
from helper_functions import utils


NUM_TEST_ELEMENTS = 10**4
# Set recursion limit (default is 1000)
sys.setrecursionlimit(NUM_TEST_ELEMENTS+10)
random.seed(42)

def count_down(n):
  """Count down from n to 1.
  @note Big 0:
    - Time complexity: O(n)
    - Space complexity: O(n)

  Parameters
  ----------
  n : int
      value to count down from
  """
  if n > 0:
    print(n)
    count_down(n-1)


def binary_search(A, left, right, K):
  """Search for K in A
  @note This is a binary search algorithm.
  - Time complexity: O(log n)
  - Space complexity: O(1)
  Usage: binary_search(A, 0, len(A)-1, K)

  Parameters
  ----------
  A : list, array...
      array to search
  left : int
      left index from which to search
  right : int
      right index from which to search
  K : value
      value to search for

  Returns
  -------
  int
      index of K in A, -1 if not found
  """
  if left == right:
    if A[left] == K:
      return left
    else:
      return -1
  else:
    mid = (left + right) // 2
    if A[mid] == K:
      return mid
    else:
      if A[mid] < K:
        return binary_search(A, mid + 1, right, K)
      else:
        return binary_search(A, left, mid - 1, K)


def greatest_common_divisor(a, b):
  """Compute the greatest common divisor of a and b.
  @note This is a recursive function.
  - Time complexity: O(log(min(a,b)))
  - Space complexity: O(1)

  Parameters
  ----------
  a : int
      value a
  b : int
      value b

  Returns
  -------
  int
      greatest common divisor of a and b
  """
  if b == 0:
    return a
  else:
    return greatest_common_divisor(b, a % b)


def insert_sort(A, k):
  """Sort array A using insertion sort algorithm
  @note This method uses recursive algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  Usage: insert_sort(A, 0)

  Parameters
  ----------
  A : list, array...
      array to sort
  k : int
      index of the element to be sorted
  """
  j = k
  while j > 0 and A[j] < A[j-1]:
    A[j], A[j-1] = A[j-1], A[j]
    j -= 1
  if k < len(A) - 1:
    insert_sort(A, k+1)


def selection_sort(A, k):
  """Sort array A using selection sort algorithm
  @note This method uses recursive algorithm.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  Usage: selection_sort(A, 0)

  Parameters
  ----------
  A : list, array...
      array to sort
  k : int
      index of the element to be sorted
  """
  if k < len(A) - 1:
    min_idx = k
    for i in range(k+1, len(A)):
      if A[i] < A[min_idx]:
        min_idx = i
    A[k], A[min_idx] = A[min_idx], A[k]
    selection_sort(A, k+1)


def polynomial_calc(A, x, k):
  """Calculate the value of polynomial A at x
  @note This is a recursive function.
  - Time complexity: O(n^2)
  - Space complexity: O(1)
  Usage: polynomial_calc(A, x, n)

  Parameters
  ----------
  A : list, array...
      array of coefficients of polynomial A
  x : int
      value of x
  k : int
      degree of current polynomial

  Returns
  -------
  int
      value of polynomial A at x

  @note An example of polynomial: A = [1, 2, 3] => A = 1 + 2*x + 3*x^2
  """  
  if k == 0:
    return A[0]
  else:
    return A[k]*(x**k) + polynomial_calc(A, x, k-1)
  

def polynomial_fast_calc(A, x, p, k):
  """Calculate the value of polynomial A at x
  @note This is a recursive function.
  - Time complexity: O(n)
  - Space complexity: O(1)
  Usage: polynomial_fast_calc(A, x, exp(x, n+1), n)

  Parameters
  ----------
  A : list, array...
      array of coefficients of polynomial A
  x : int
      value of x
  p : int
      value of x^(k+1)
  k : int
      degree of current polynomial

  Returns
  -------
  int
      value of polynomial A at x

  @note An example of polynomial: A = [1, 2, 3] => A = 1 + 2*x + 3*x^2
  """
  if k == 0:
    return A[0]
  else:
    p = p/x
    return A[k]*p + polynomial_fast_calc(A, x, p, k-1)


def polynomial_horner_calc(A, x, k):
  """Calculate the value of polynomial A at x
  @note Using Horner algorithm with recursion.
  - Time complexity: O(n)
  - Space complexity: O(1)
  Usage: polynomial_horner_calc(A, x, 0)

  Parameters
  ----------
  A : list, array...
      array of coefficients of polynomial A
  x : int
      value of x
  k : int
      degree of current polynomial

  Returns
  -------
  int
      value of polynomial A at x

  @note An example of polynomial: A = [1, 2, 3] => A = 1 + 2*x + 3*x^2
  """
  # degree of polynomial A
  n = len(A) - 1
  if k == n:
    return A[n]
  else:
    return A[k] + x*polynomial_horner_calc(A, x, k+1)


def hanoi(n, i, j, k):
  """Solve Tower of Hanoi problem
  @note Big O:
  - Time complexity: O(2^n)
  - Space complexity: O(1)
  Usage: In case n = 3 --> hanoi(3, 0, 2, 1)

  Parameters
  ----------
  n : int
      number of disks
  i : int
      index of the source tower
  j : int
      index of the destination tower
  k : int
      index of the auxiliary tower
  """
  if n > 0:
    hanoi(n-1, i, k, j)
    print(f"Move disk {n} from {i} to {j}")
    hanoi(n-1, k, j, i)


def permute_generation(n):
  """Generate all permutations of n
  @note Big O:
  - Time complexity: O(n!)
  - Space complexity: O(n!)
  Usage: permute_generation(n)

  Parameters
  ----------
  n : int
      number of elements

  Returns
  -------
  list
      list of permutations
  """

  def insert_all(n, A):
    """Insert n into all possible positions of A

    Parameters
    ----------
    n : int
        number to insert
    A : list
        list to insert into

    Returns
    -------
    list
        list of permutations
    """
    new = []
    for i in range(len(A)+1):
      B = A.copy()
      B.insert(i, n)
      new.append(B)
      print(f'==n = {n}, A = {A}, i = {i}, B = {B}, new = {new}==')
    return new

  def generate(n):
    """Generate all permutations of n

    Parameters
    ----------
    n : int
        number of elements

    Returns
    -------
    list
        list of permutations
    """
    if n == 1:
      return [[1]]
    else:
      new = []
      A = generate(n-1)
      print(f'n = {n}, A = {A}')
      for p in A:
        new = new + insert_all(n, p)
        print(f'n = {n}, p = {p}, new = {new}')
      return new

  return generate(n)


def permute(A, k):
  """Generate all permutations of A
  @note This method uses recursive algorithm.
  - Time complexity: O(n!)
  - Space complexity: O(n!)
  Usage: permute(A, 0)

  Parameters
  ----------
  A : list, array...
      array to permute
  k : int
      index of the element to be permuted
  """
  n = len(A)
  A = A.copy()
  print(f'\n==k = {k}, A = {A}==')
  if k == n-1:
    print(A)
  else:
    for i in range(k, n):
      A[k], A[i] = A[i], A[k]
      print(f'k = {k}, i = {i}, A = {A}')
      permute(A, k+1)


"""Implement test cases here
"""

def test_gcd():
  """Test greatest_common_divisor function
  """
  print("== Test greatest_common_divisor function ==")
  # create dict array with:
  # - random value a and b in range [0, 10**5]
  # - the greatest common divisor of a and b
  num_test = 10
  test_log = [{} for i in range(num_test)]
  test_range = 10**2
  for i in range(num_test):
    a = random.randint(0, test_range)
    b = random.randint(0, test_range)
    test_log[i] = {"a":a, "b":b, "gcd":greatest_common_divisor(a, b)}
  
  test_log_df = pd.DataFrame(test_log, columns=test_log[0].keys())
  print(f"Test log:\n {test_log_df}")

  # Recheck the results, if failed, raise AssertionError and print the test log
  for i in range(num_test):
    assert test_log[i]["gcd"] == gcd(test_log[i]["a"], test_log[i]["b"]),\
      f"Test failed at {i}th test case with a = {test_log[i]['a']}, b = {test_log[i]['b']}, gcd = {test_log[i]['gcd']}"
  print("Test passed")


if __name__ == '__main__':
  # Test count_down function
  utils.test_alg_func_num(count_down, NUM_TEST_ELEMENTS)
  print("\n")

  # Test binary_search function
  utils.test_search_func(binary_search, NUM_TEST_ELEMENTS, is_recursive = True)
  print("\n")

  # Test greatest_common_divisor function
  test_gcd()
  print("\n")

  # test insert_sort
  utils.test_sort_func(insert_sort, NUM_TEST_ELEMENTS, is_recursive = True, istart = 0)
  print("\n")

  # test selection_sort
  utils.test_sort_func(selection_sort, NUM_TEST_ELEMENTS, is_recursive = True, istart = 0)
  print("\n")

  degree = 2
  # test polynomial_calc
  utils.test_polynomial_func(polynomial_calc,
                              x=4,
                              n=degree,
                              k_start=degree,
                              coeff_max=3,
                              num_test=10)
  print("\n")

  # test polynomial_horner_calc
  utils.test_polynomial_func(polynomial_horner_calc,
                              x=4,
                              n=degree,
                              k_start=0,
                              coeff_max=3,
                              num_test=10)
  print("\n")

  # test permute_generation
  n = 3
  print(f"== Test permute_generation function with n = {n} ==")
  all = permute_generation(n)
  print(f"Number of permutations: {len(all)}")
  print("Permutations:")
  [print(p) for p in all]
  print("\n")

  # test permute
  n = 4
  print(f"== Test permute function with n = {n} ==")
  A = [i for i in range(1, n+1)]
  permute(A, 0)
  print("\n")



