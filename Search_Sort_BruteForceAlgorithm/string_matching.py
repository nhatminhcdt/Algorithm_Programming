import random
from time import perf_counter
# Import local
import sys, os
sys.path.append(os.getcwd())
from helper_functions import utils

NUM_TEST_CHARS = 100
NUM_MATCH_CHAR = 10

def string_matching(T, P):
  """@brief Search for P in T
  @note This is a string matching algorithm.
  - Time complexity: O(nm)
  - Space complexity: O(1)
  @param T : string
      text
  @param P : string
      pattern to search for
  @return int
      index of P in T, -1 if not found
  """
  n = len(T)
  m = len(P)
  for k in range(n-m+1):
    j = 0
    while j < m and P[j] == T[k+j]:
      j += 1
    if j == m:
      return k
  return -1


"""@brief Implement test function for string matching algorithm
"""
def test_string_matching(n:int):
  # Create random text and pattern
  T = utils.generate_random_string(n)
  # Select a random index in T
  k = random.randint(0, n-NUM_MATCH_CHAR)
  P = T[k:k+NUM_MATCH_CHAR]
  # Test string_matching
  start = perf_counter()
  index = string_matching(T, P)
  end = perf_counter()
  # Print results
  print("T: ", T)
  print("P: ", P)
  print("index: ", index)
  print("Time: ", end-start, "s")


if __name__ == "__main__":
  test_string_matching(NUM_TEST_CHARS)
