from collections import Counter
from collections import OrderedDict

class LeagueTable:
  """
  Class LeagueTable created to storage players and their scores and games played.
  """

  def __init__(self, players:list):
    """
    Args:
      players (list): A list of all the players names.
    """
    self.standings = OrderedDict([(player, Counter({"position": counter + 1})) for player, counter in zip(players, range(len(players)))])
      
  def record_result(self, player:str, score:int):
    """
    A function used to storage the player score of a game played.

    Args:
      player (str): A string containing the name of the player.
      score (int): A integer with the player score.
    """
    if type(player) != str: raise Exception("The player name must be a string!")
    if self.standings.get(player) == None: raise Exception("This player name is not among the league players!")
    if type(score) != int: raise Exception("The player score must be a integer!")

    self.standings[player]["games_played"] += 1
    self.standings[player]["score"] += score
    
  def player_rank(self, rank:int) -> str:
    """
    A function used to return the player name at a specific ranking position.

    Args:
      rank (int): The requested ranking position.
    
    Returns:
      (str): Player name in the specific ranking position.
    """
    if type(rank) != int: raise Exception("The ranking position must be a integer!")
    if rank < 1 or rank > len(self.standings): raise Exception("This ranking position does not exist!")
    
    ranking = sorted(self.standings, key=lambda p: (-self.standings[p]["score"], self.standings[p]["games_played"], self.standings[p]["position"]))
    return ranking[rank - 1]
          

if __name__ == "__main__":
  table = LeagueTable(["Mike", "Chris", "Arnold"])
  table.record_result("Mike", 2)
  table.record_result("Mike", 3)
  table.record_result("Arnold", 5)
  table.record_result("Chris", 5)
  print(table.player_rank())