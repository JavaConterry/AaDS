from Array import Array
from LinkedList import BiLinkedList

input_data = input('Input the data:')
array_data = Array(input_data)

list_data = BiLinkedList()
list_data.read(input_data)

print(list_data.tail.previous.value)
list_data.add(3, 'NO')

print(str(list_data))