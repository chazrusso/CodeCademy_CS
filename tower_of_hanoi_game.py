
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


class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

#Initial message for the user
print("\nLet's play Towers of Hanoi!!")

#Stack creation
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?"))

#We want the number of disks to be greater than or equal to 3. This will ask for a number less than 3
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

#Add all disks to the left stack. The higher number disk is larger, so we itterate backwards through num_disks
for disk in range(num_disks, 0 , -1):
  left_stack.push(disk)

#Number of optimal moves = 2^(num_disks) - 1
num_optimal_moves = 2**(num_disks) - 1

#Taunt the user with the following message
print("\nThe fastest you can solve this game is in {moves} moves".format(moves = num_optimal_moves))

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('Enter {letter} for {name}'.format(letter = letter, name = name))

    user_input = input()

    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
       
#Play the Game
num_user_moves = 0
while (right_stack.get_size() != num_disks):
  print("\n\n\n...Currrent Stacks...")

  for i in range(len(stacks)):
    stacks[i].print_items()
  
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()

    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again.")

    elif to_stack.is_empty() or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break

    else:
      print("\n\nInvalid Move. Try Again.")

print("\n\nYou completed the game in {player_moves} moves, and the optimal number of moves is {optimal}".format(player_moves = num_user_moves, optimal = num_optimal_moves))