import pytest

from LeagueTable import LeagueTable


def test_correct_answer():
  """
  Tests possibilities of parameter inputs and their returns.
  """
  table = LeagueTable(["Mike", "Chris", "Arnold"])
  
  table.record_result("Mike", 2)
  with pytest.raises(Exception): table.record_result("Mik", 2)
  table.record_result("Mike", 3)
  table.record_result("Arnold", 5)
  with pytest.raises(Exception): table.record_result("Arnold", [10])
  table.record_result("Chris", 5)
  with pytest.raises(Exception): table.record_result(2, "Chris")
  
  assert table.player_rank(1) == "Chris"
  assert table.player_rank(2) == "Arnold"
  assert table.player_rank(3) == "Mike"
  with pytest.raises(Exception): table.player_rank(-8)
  with pytest.raises(Exception): table.player_rank(0)
  with pytest.raises(Exception): table.player_rank(4)
  with pytest.raises(Exception): table.player_rank(999)
  with pytest.raises(Exception): table.player_rank("position")


def test_players_have_different_scores():
  """
  Test possibilities using multiple players where everyone has different scores.
  """
  table = LeagueTable(["Mike", "Chris", "Arnold", "Khadija", "Leonor", "Patrícia", "Elói", "Oriana"])
  
  table.record_result("Mike", 2)
  table.record_result("Arnold", 3)
  table.record_result("Chris", 8)
  table.record_result("Khadija", 1)
  table.record_result("Patrícia", 5)
  table.record_result("Elói", 4)
  table.record_result("Leonor", 7)
  table.record_result("Oriana", 6)
  
  assert table.player_rank(1) == "Chris"
  assert table.player_rank(2) == "Leonor"
  assert table.player_rank(3) == "Oriana"
  assert table.player_rank(4) == "Patrícia"
  assert table.player_rank(5) == "Elói"
  assert table.player_rank(6) == "Arnold"
  assert table.player_rank(7) == "Mike"
  assert table.player_rank(8) == "Khadija"

def test_players_tied_by_score():
  """
  Test possibilities using multiple players where everyone has the same score.
  """
  table = LeagueTable(["Mike", "Chris", "Arnold", "Khadija", "Leonor", "Patrícia", "Elói", "Oriana"])

  table.record_result("Mike", 3)
  table.record_result("Mike", 2)
  table.record_result("Arnold", 1)
  table.record_result("Arnold", 4)
  table.record_result("Arnold", 0)
  table.record_result("Chris", 5)
  table.record_result("Khadija", 2)
  table.record_result("Khadija", 3)
  table.record_result("Patrícia", 1)
  table.record_result("Patrícia", 3)
  table.record_result("Patrícia", 1)
  table.record_result("Elói", 4)
  table.record_result("Elói", 1)
  table.record_result("Leonor", 1)
  table.record_result("Leonor", 1)
  table.record_result("Leonor", 2)
  table.record_result("Leonor", 1)
  table.record_result("Oriana", 1)
  table.record_result("Oriana", 1)
  table.record_result("Oriana", 1)
  table.record_result("Oriana", 1)
  table.record_result("Oriana", 1)

  assert table.player_rank(1) == "Chris"
  assert table.player_rank(2) == "Mike"
  assert table.player_rank(3) == "Khadija"
  assert table.player_rank(4) == "Elói"
  assert table.player_rank(5) == "Arnold"
  assert table.player_rank(6) == "Patrícia"
  assert table.player_rank(7) == "Leonor"
  assert table.player_rank(8) == "Oriana"

def test_players_tied_by_games_played():
  """
  Test possibilities using multiple players where everyone has the same quantity of games played.
  """
  table = LeagueTable(["Mike", "Chris", "Arnold", "Khadija", "Leonor", "Patrícia", "Elói", "Oriana"])

  table.record_result("Mike", 5)
  table.record_result("Mike", 2)
  table.record_result("Arnold", 1)
  table.record_result("Arnold", 6)
  table.record_result("Chris", 6)
  table.record_result("Chris", 0)
  table.record_result("Khadija", 9)
  table.record_result("Khadija", 4)
  table.record_result("Patrícia", 2)
  table.record_result("Patrícia", 1)
  table.record_result("Elói", 4)
  table.record_result("Elói", 7)
  table.record_result("Leonor", 3)
  table.record_result("Leonor", 3)
  table.record_result("Oriana", 8)
  table.record_result("Oriana", 5)

  assert table.player_rank(1) == "Khadija"
  assert table.player_rank(2) == "Oriana"
  assert table.player_rank(3) == "Elói"
  assert table.player_rank(4) == "Mike"
  assert table.player_rank(5) == "Arnold"
  assert table.player_rank(6) == "Chris"
  assert table.player_rank(7) == "Leonor"
  assert table.player_rank(8) == "Patrícia"
