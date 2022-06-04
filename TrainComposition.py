from collections import deque

class TrainComposition:
  """
  Class TrainComposition created to attach and detach wagons of the train.
  """
  
  def __init__(self):
    self.wagons_order = deque([])
  
  def attach_wagon_from_left(self, wagonId:int):
    """
    A function used to add a wagon id in the left of deque data structure.

    Args:
      wagonId (int): The number of the wagon to attach to the left.
    """
    if type(wagonId) != int: raise Exception("The wagonId has to be a integer!")
    self.wagons_order.appendleft(wagonId)
  
  def attach_wagon_from_right(self, wagonId:int):
    """
    A function used to add a wagon id in the right of deque data structure.

    Args:
      wagonId (int): The number of the wagon to attach to the right.
    """
    if type(wagonId) != int: raise Exception("The wagonId has to be a integer!")
    self.wagons_order.append(wagonId)

  def detach_wagon_from_left(self) -> int:
    """
    A function used to remove and return a wagon id in the left of deque data structure.

    Returns:
      (int): The number of the wagon detached from left.
    """
    try:
      return self.wagons_order.popleft()
    except IndexError:
      raise Exception("The train is empty. Unable to remove a wagon!")

  def detach_wagon_from_right(self) -> int:
    """
    A function used to remove and return a wagon id in the right of deque data structure.

    Returns:
      (int): The number of the wagon detached from right.
    """
    try:
      return self.wagons_order.pop()
    except IndexError:
      raise Exception("The train is empty. Unable to remove a wagon!")

if __name__ == "__main__":
  train = TrainComposition()
  train.attach_wagon_from_left(7)
  train.attach_wagon_from_left(13)
  print(train.detach_wagon_from_right())
  print(train.detach_wagon_from_left())