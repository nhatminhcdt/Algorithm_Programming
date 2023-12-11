import string
import random
from random import randint
from time import perf_counter

def create_array(n: int):
  """Create an array of size n
  @remark This function creates an array of size n with random values in range [0, n].
  
  Parameters
  ----------
  n : int
      size of array
  
  Returns
  -------
  list
      array of size n
  """
  A = [randint(-n, n) for i in range(n)]
  return A


def create_sorted_array_and_selected_value(n: int):
  """Create an array of size n
  @remark This function creates an array of size n with random values
  in range [0, n] and sorted. Then, it chooses a random value in the array.

  Parameters
  ----------
  n : int
      size of array

  Returns
  -------
  list
      array of size n
  int
      random value in the array
  """
  # Create random array but sorted
  A = sorted([randint(0, n) for i in range(n)])
  # Choose a random value in A
  K = A[randint(0, n)]
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


def test_sort_func(alg_func, n: int):
  """@brief Test the above functions
  @param alg_func : function
      algorithm function
  @param n : int
      number of elements in the array
  """
  # Extract the name of the input function
  alg_name = alg_func.__name__
  # Test insertion_sort
  A = create_array(n)
  # print first 10 elements of A and 10 last elements of A before sorting
  print("A[:10] before sorting: ", A[:10])
  print("A[-10:] before sorting: ", A[-10:])
  start = perf_counter()
  alg_func(A)
  exec_time =perf_counter() - start
  # print first 10 elements of A and 10 last elements of A after sorting
  print("A[:10] after sorting: ", A[:10])
  print("A[-10:] after sorting: ", A[-10:])
  print("%s: %.2f(s)" % (alg_name, exec_time))
  exec_time = round(exec_time, 2)
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