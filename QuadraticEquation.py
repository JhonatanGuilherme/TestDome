from math import sqrt


def find_roots(a: int, b: int, c: int) -> tuple:
  """
  A function used to find roots of a quadratic equation.

  Args:
    a (int): A value that multiplies x^2.
    b (int): A value that multiplies x.
    c (int): A constant.
  
  Returns:
    (tuple): A tuple with two possible roots to the quadratic equation.
  """
  if a == 0: raise Exception("The value of variable 'a' can not be 0!")
  
  delta = b ** 2 - 4 * a * c
  delta_sqrt = sqrt(delta)

  root_one = (-b + delta_sqrt) / (2 * a)
  root_two = (-b - delta_sqrt) / (2 * a)
  
  return (root_one, root_two)
    

print(find_roots(2, 10, 8))
