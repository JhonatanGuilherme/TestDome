import pytest

from RoutePlanner import route_exists

def test_correct_answer():
  """
  Tests possibilities of parameter inputs and their returns.
  """
  map_matrix = [[True, False, False],
                [True, True, False],
                [False, True, True]]
  
  assert route_exists(0, 0, 2, 2, map_matrix) == True
  assert route_exists(2, 2, 0, 0, map_matrix) == True
  assert route_exists(0, 1, 2, 1, map_matrix) == False
  with pytest.raises(Exception): route_exists(0, 4, 4, 5, map_matrix)
  with pytest.raises(Exception): route_exists("0", "0", "2", "2", map_matrix)

def test_various_routes_from_top_left_to_bottom_right_corner():
  """
  Test possibilities of paths starting from the upper left corner to the lower right corner.
  """
  map_matrix = [[True, False, True, False],
                [True, True, True, False],
                [False, True, True, False],
                [False, False, True, True]]
  
  assert route_exists(0, 0, 3, 3, map_matrix) == True

  map_matrix = [[True, False, True, False, False],
                [True, True, True, False, True],
                [False, True, True, False, True],
                [False, False, True, True, True],
                [True, True, True, False, True]]

  assert route_exists(0, 0, 4, 4, map_matrix) == True

  map_matrix = [[True, False, True, False, False, False],
                [True, True, True, False, True, True],
                [False, True, True, False, True, False],
                [False, False, True, False, True, False],
                [True, True, True, False, True, False],
                [False, False, True, True, True, True]]
  
  assert route_exists(0, 0, 5, 5, map_matrix) == True

  map_matrix = [[True, False, True, False, False, False, False],
                [True, True, True, False, True, True, False],
                [False, True, True, False, True, False, True],
                [False, False, True, False, True, False, True],
                [True, True, True, True, True, True, False],
                [False, False, True, True, False, True, True]]
  
  assert route_exists(0, 0, 5, 6, map_matrix) == True
  with pytest.raises(Exception): route_exists(0, 0, 6, 5, map_matrix)
  

def test_various_routes_starts_and_destinations():
  """
  Test possibilities of paths starting and ending at any positions.
  """
  map_matrix = [[True, False, True, False, False, False, False],
                [True, True, True, False, True, True, False],
                [False, True, True, False, True, False, True],
                [False, False, True, False, True, False, True],
                [True, True, True, True, True, True, False],
                [False, False, True, True, False, True, True],
                [False, False, True, False, False, True, True]]
  
  assert route_exists(2, 2, 0, 0, map_matrix) == True
  assert route_exists(2, 1, 1, 4, map_matrix) == True
  assert route_exists(2, 2, 5, 5, map_matrix) == True
  assert route_exists(5, 6, 4, 5, map_matrix) == True
  assert route_exists(1, 0, 0, 0, map_matrix) == True
  assert route_exists(2, 2, 1, 5, map_matrix) == True
