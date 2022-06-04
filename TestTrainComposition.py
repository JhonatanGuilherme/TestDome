import pytest

from TrainComposition import TrainComposition

train = TrainComposition()

def test_correct_answer():
  """
  Tests possibilities of parameter inputs and their returns.
  """
  train.attach_wagon_from_left(7)
  train.attach_wagon_from_left(13)
  assert train.detach_wagon_from_right() == 7
  assert train.detach_wagon_from_left() == 13

  train.attach_wagon_from_left(0)
  train.attach_wagon_from_left(1)
  with pytest.raises(Exception): train.attach_wagon_from_left("a")
  with pytest.raises(Exception): train.attach_wagon_from_right([1])
  train.attach_wagon_from_left(2)
  train.attach_wagon_from_right(3)
  assert train.detach_wagon_from_left() == 2
  assert train.detach_wagon_from_right() == 3
  assert train.detach_wagon_from_left() == 1
  assert train.detach_wagon_from_right() == 0
  with pytest.raises(Exception): assert train.detach_wagon_from_left() == None
  with pytest.raises(Exception): assert train.detach_wagon_from_right() == None


def test_several_wagons():
  """
  Test possibilities with multiple wagons attached and detached.
  """
  for i in range(99999):
    train.attach_wagon_from_left(i)
  for j in range(99999):
    assert train.detach_wagon_from_right() == j
