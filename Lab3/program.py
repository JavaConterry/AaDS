from Array import Array
from LinkedList import BiLinkedList


def is_valid_str(str):
    for i in str:
        ch = chr(i)
        if(not ((ch>64 and ch<91) or (ch>96 and ch<123) or ch==46)):
            return False
    return True

def read_input_text():
    input_data = input('Input the data:')

    if(input_data == ''):
        print('Given an empty text, please try again')
        return read_input_text()
    if(not is_valid_str(input_data)):
        print('Your text contains invalid text charchter')
        return read_input_text()



input_data = read_input_text()

array_data = Array(input_data)

list_data = BiLinkedList()
list_data.read(input_data)

print(list_data.tail.previous.value)
list_data.add(3, 'NO')

print(str(list_data))


# DSs require unit tests