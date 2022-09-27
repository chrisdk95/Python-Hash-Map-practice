from linked_list import Node, LinkedList
from blossom_lib import flower_definitions
class HashMap:
  def __init__(self, size):
    self.array_size = size #array needed(python list)
    self.array = [LinkedList() for i in range(self.array_size)]
  
  #4 methods needed for hash map. 2 internal .hash() & .compress, and 2 external .assign() and .compress()
  def hash(self, key): #when key is a string, calculate a number for string
    return sum(key.encode()) #performs a sum on the resulting list-like object

  def compress(self, hash_code): #reduces number into array index
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key)) #get hash code by plugging key into .hash() and array index by plugging hash code into .compress()
    payload = Node([key, value])
    list_at_array = self.array[array_index] #to see if key exists before adding new payload
    for i in list_at_array: #check if the key[0] is same as the key we're trying to assign
      if key == i[0]:
        i[1] = value #overwrite value if key is found
        return
    list_at_array.insert(payload) #add if key is not found

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    payload = self.array[array_index]
    list_at_index = self.array[array_index] #linkedlist object at that index in self.array
    for i in list_at_index:
      if key == i[0]: #checiking to see if it's the same as key
        return i[1] #if key is found, return value at index 1
      else:
        return None #if not found
blossom = HashMap(len(flower_definitions)) #to make list of HashMap be same length as flower definitions
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1]) #assign value (index 1) to its key (index 0)
print(blossom.retrieve('daisy'))
