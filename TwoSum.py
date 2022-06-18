def find_two_sum(numbers: list, target_sum: int):
  """
  Args:
    numbers (list of ints): The list of numbers.
    target_sum (int): The required target sum.
  
  Returns:
    (tuple): The indices of the two elements whose sum is equal to target_sum.
  """
  numbers_dict = {}
  for i, number in enumerate(numbers):
    diff = target_sum - number
    if diff in numbers_dict:
        return (i, numbers_dict[diff])
    numbers_dict[number] = i

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))