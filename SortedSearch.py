def count_numbers(sorted_list: list, less_than: int):
  previous_middle_index = -1
  start_index = 0
  end_index = len(sorted_list)
  while True:
    middle_index = (start_index + end_index) // 2
    if middle_index == previous_middle_index:
      return 0
    if sorted_list[middle_index] < less_than:
      if middle_index == len(sorted_list) - 1 or sorted_list[middle_index + 1] >= less_than:
        return middle_index + 1
      start_index = middle_index
    else:
      if sorted_list[middle_index - 1] < less_than:
        return middle_index
      end_index = middle_index + 1
    previous_middle_index = middle_index

if __name__ == "__main__":
  sorted_list = [1, 3, 5, 7]
  print(count_numbers(sorted_list, 4)) # should print 2