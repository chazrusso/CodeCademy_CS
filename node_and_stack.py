#Node class creation: create a node with a set value. Previous and Next nodes default to 'None'
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
#Set the 'next node' in the list to a new node    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
#Return the value of the next node in the list    
  def get_next_node(self):
    return self.next_node

#Set the 'previous node' in the list to a new node
  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
#Return the value of the previous node    
  def get_prev_node(self):
    return self.prev_node

#Return the value of the current node  
  def get_value(self):
    return self.value

#Stacks are LIFO - last in, first out
#Creation of stack class
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

#push adds to the top of the stack  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

#Pop returns and removes the top item of the stack
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

#Peek returns the top item without removing it
  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

#has_space tealls if there is room for another item - prevents overflow
  def has_space(self):
    return self.limit > self.size

#is_empty shows if the stack is empty - prevents underflow
  def is_empty(self):
    return self.size == 0
  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.pop()
