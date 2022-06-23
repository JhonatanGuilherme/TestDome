import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value: int):
    actual_node = root
    if actual_node == None:
      return False
    elif actual_node.value == value:
      return True
    elif actual_node.value > value:
      return contains(actual_node.left, value)
    else:
      return contains(actual_node.right, value)
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))