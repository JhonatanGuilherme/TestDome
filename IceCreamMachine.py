class IceCreamMachine:
  """Ice Cream Machine class."""
    
  def __init__(self, ingredients, toppings):
    """
    Args:
      ingredients (list): A list with ice cream ingredients.
      toppings (list): A list with ice cream toppings.
    """
    self.ingredients = ingredients
    self.toppings = toppings
    
  def scoops(self):
    """
    Get all possible combinations with ingredients and topping to make ice creams.

    Returns:
      possible_combinations (list): A matrix with combination lists containing ingredients and toppings.
    """
    possible_combinations = []
    for i in range(len(self.ingredients)):
      for j in range(len(self.toppings)):
        possible_combinations.append([self.ingredients[i], self.toppings[j]])
    return possible_combinations

if __name__ == "__main__":
  machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
  print(machine.scoops())