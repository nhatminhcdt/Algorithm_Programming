import string
import random
import pandas as pd
from numpy import polyval
from time import perf_counter

random.seed(42)


def create_array(min_val, max_val, n: int, is_dupplicate: bool = True):
  """Create an array of size n
  @remark This function creates an array of size n with random values in range [0, n].
  
  Parameters
  ----------
  min_val : int
      minimum value of the array
  max_val : int
      maximum value of the array
  n : int
      size of array
  is_dupplicate : bool
      True if the array can have dupplicate values, False otherwise
  
  Returns
  -------
  list
      array of size n
  """
  if is_dupplicate:
    A = [random.randint(min_val, max_val) for i in range(n)]
  else:
    if n > max_val - min_val:
      A = []
      while len(A) < n:
        a = random.randint(min_val, max_val)
        if a not in A:
          A.append(a)
    else:
      raise ValueError("n must be greater than max_val - min_val")
    
  return A


def create_sorted_array_and_selected_value(min_val, max_val, n: int, is_dupplicate: bool = True):
  """Create an array of size n
  @remark This function creates an array of size n with random values
  in range [0, n] and sorted. Then, it chooses a random value in the array.

  Parameters
  ----------
  min_val : int
      minimum value of the array
  max_val : int
      maximum value of the array
  n : int
      size of array
  is_dupplicate : bool
      True if the array can have dupplicate values, False otherwise

  Returns
  -------
  list
      array of size n
  int
      random value in the array
  """
  if is_dupplicate:
    A = [random.randint(min_val, max_val) for i in range(n)]
    A.sort()
  else:
    if n > max_val - min_val:
      A = []
      while len(A) < n:
        a = random.randint(min_val, max_val)
        if a not in A:
          A.append(a)
      A.sort()
    else:
      raise ValueError("n must be greater than max_val - min_val")
    
  # Choose a random value in A
  K = A[random.randint(0, n)]

  return A, K


def generate_random_string(length):
  """Generate a random string of fixed length
  Parameters
  ----------
  length : int
      length of the string

  Returns
  -------
  string
      random string of fixed length
  """
  characters = string.ascii_letters + string.digits
  random_string = ''.join(random.choice(characters) for i in range(length))

  return random_string


def test_search_func(alg_func, n: int, is_recursive: bool = False):
  """Test functions with search algorithm
  @param alg_func : function
      algorithm function
  @param n : int
      number of elements in the array
  @param is_recursive : bool
      True if the algorithm is recursive, False otherwise
  """
  # Extract the name of the input function
  alg_name = alg_func.__name__
  print(f"==Test {alg_name} function==")
  A, K = create_sorted_array_and_selected_value(-n, n, n, True)
  print(f"A: {A[:10]}...{A[-10:]}\nK: {K}")

  # Test binary_search function
  start = perf_counter()
  if is_recursive == True:
    index = alg_func(A, 0, len(A)-1, K)
  else:
    index = alg_func(A, K)
  exec_time = round(perf_counter() - start, 2)
  print(f"binary_search: {exec_time} seconds")
  if index != -1:
    print(f"index: {index}, value: {A[index]}")
  else:
    print("Not found")

  # Test in-built function
  start_ = perf_counter()
  index_verify = A.index(K)
  end_ = perf_counter()
  print(f"Built-in (index) search: {end_-start_:.2f} seconds")

  # Recheck the results, if failed, raise AssertionError and print the test log
  assert A[index] == A[index_verify],\
    f"Test failed: index = {index} value = {A[index]}, index_verify = {index_verify} value = {A[index_verify]}"
  print("Test passed\n")

  return [alg_name, exec_time]
  

def test_sort_func(alg_func, n: int, is_recursive: bool = False, istart : int = 0):
  """Test sort function
  @note This function tests the sort function by creating a random array, activate the sort function, then compare the result with the in-built function.

  @param alg_func : function
      algorithm function
  @param n : int
      number of elements in the array
  @param is_recursive : bool
      True if the algorithm is recursive, False otherwise
  @param istart : int
      index of the element to be sorted
  """
  func_name = alg_func.__name__
  print(f"==Test {func_name} function==")
  # Create random array

  A_ORG = create_array(-n, n, n, True)
  print(f"A_ORG: {A_ORG[:10]}...{A_ORG[-10:]}")

  # Test insert_sort function
  A = A_ORG.copy()
  start = perf_counter()
  if is_recursive:
    alg_func(A, istart)
  else:
    alg_func(A)
  exec_time = round(perf_counter() - start, 2)
  print(f"{func_name}: {exec_time} seconds")
  print(f"A after sorted: {A[:10]}...{A[-10:]}")

  # Test in-built function
  A_verify = A_ORG.copy()
  start = perf_counter()
  A_verify = sorted(A_verify)
  print(f"sorted: {perf_counter()-start:.2f} seconds")
  print(f"A_verify after sorted: {A_verify[:10]}...{A_verify[-10:]}")

  # Recheck the results, if failed, raise AssertionError and print the test log
  assert A == A_verify,\
    f"Test failed:\nA = {A}\nA_verify = {A_verify}"
  print("Test passed")

  return [func_name, exec_time]


def test_alg_func_num(alg_func, n: int):
  """@brief Test the above functions
  @param alg_func : function
      algorithm function
  @param n : int
      number of elements in the array
  """
  # Extract the name of the input function
  alg_name = alg_func.__name__
  start = perf_counter()
  alg_func(n)
  exec_time = perf_counter() - start
  exec_time = round(exec_time, 2)
  print("%s: %.2f(s)" % (alg_name, exec_time))

  return [alg_name, exec_time]


def test_alg_func(alg_func, *args, **kwargs):
  """@brief Test the above functions
  @param alg_func : function
      algorithm function
  @param *args : list
      list of arguments
  @param **kwargs : dict
      dictionary of arguments
  """
  # Extract the name of the input function
  alg_name = alg_func.__name__

  # Get the arguments of the input function
  # Check if *args is empty
  if args:
    start = perf_counter()
    ret = alg_func(*args)
    end = perf_counter()

  # Check if **kwargs is empty
  elif kwargs:
    start = perf_counter()
    ret = alg_func(**kwargs)
    end = perf_counter()
  else:
    raise ValueError("Both *args and **kwargs are empty")
  exec_time = end - start

  # Print execution time
  print("%s: %.2f(s)" % (alg_name, exec_time))
  exec_time = round(exec_time, 2)

  return alg_name, exec_time, ret


def test_polynomial_func(alg_func, x: int, n: int = 3, k_start: int = 0, coeff_max: int = 10, num_test: int = 10):
  """Test polynomial evaluation functions
  @param alg_func : function
      algorithm function
  @param x : int
      value of x
  @param n : int
      degree of polynomial
  @param k_start : int
      starting index of coefficients
  @param coeff_max : int
      maximum value of coefficients
  @param num_test : int
      number of test cases

  Returns
  -------
  DataFrame
      test log

  @note An example of polynomial: A = [1, 2, 3] => A = 1 + 2*x + 3*x^2
  """
  func_name = alg_func.__name__
  print(f"==Test {func_name} function==")
  # create dict array with:
  # - random value a and b in range [0, 10**5]
  # - the greatest common divisor of a and b
  test_log = [{} for i in range(num_test)]
  for i in range(num_test):
    start = perf_counter()
    A = [random.randint(1, coeff_max+1) for i in range(n+1)]
    X_TEST = random.randint(0, 10)
    result = alg_func(A, X_TEST, k_start)
    test_log[i] = {"A":A, "x":X_TEST, "n":n, "polynomial result":result, "Execution time":round(perf_counter() - start, 2)}
  
  test_log_df = pd.DataFrame(test_log, columns=test_log[0].keys())
  print(f"Test log:\n {test_log_df}")

  # Recheck the results, if failed, raise AssertionError and print the test log
  for i in range(num_test):
    # Reverse the order of coefficients to use numpy.polyval
    coeff = test_log_df["A"][i][::-1]
    poly_verify = polyval(coeff, test_log_df["x"][i])
    assert test_log[i]["polynomial result"] == poly_verify,\
      f"Test failed at {i}th test case with A = {test_log_df['A'][i]}, x = {test_log_df['x'][i]}, n = {test_log_df['n'][i]}, polynomial result = {test_log_df['polynomial result'][i]}, poly verify = {poly_verify}"
  print("Test passed")

  return test_log_df