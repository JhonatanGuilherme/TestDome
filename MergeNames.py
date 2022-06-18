def unique_names(names1: list, names2: list) -> list:
  """
  Returns the sum of two lists without repetitions.

  Args:
    names1 (list): The first list with string values to concatenate.
    names2 (list): The second list with string values to concatenate.
  
  Returns:
    (list): A concatenated list of received lists with no repeated values.
  """
  return sorted(list(set(names1 + names2)))

if __name__ == "__main__":
  names1 = ["Ava", "Emma", "Olivia"]
  names2 = ["Olivia", "Sophia", "Emma"]
  print(unique_names(names1, names2))