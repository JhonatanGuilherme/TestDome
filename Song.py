class Song:
  """
  Class Song created to store the actual and next songs in a playlist.
  """
  def __init__(self, name: str):
    """
    Args:
      name (str): The name of the song.
    """
    self.name = name
    self.next = None

  def next_song(self, song):
    """
    Set the next song.

    Args:
      song (Song): Song object.
    """
    self.next = song 
  
  def is_repeating_playlist(self):
    """
    Checks if the playlist is cycled or not.

    Returns:
      (bool): True if the playlist is repeating, False if not.
    """
    linked_set = set()
    current_song = self
    while current_song not in linked_set:
      next_song = current_song.next
      if next_song == None:
        return False
      linked_set.add(current_song)
      current_song = next_song
    return True
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())