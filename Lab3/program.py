from LinkedList import BiLinkedList


def is_valid_str(str):
    for i in str:
        ch = ord(i)
        if(not ((ch>64 and ch<91) or (ch>96 and ch<123) or ch==46 or ch==32)):
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
    return input_data



input_data = read_input_text()


# Using Bilinked List
list_data = BiLinkedList()
list_data.read(input_data)

result_list = BiLinkedList()

alphabet_list = BiLinkedList()
word=''
for i in range(97, 122): 
    word += chr(i)
    alphabet_list.addLast(word)

first_word = list_data.get(0)
for i in range(1, list_data.length+1):
    word = list_data.get(i)
    if(alphabet_list.has(word) and word!=first_word):
        result_list.addLast(word)
print('\nAlphabetical words which do not coincide with the first:', result_list)

count_odd = 0
for i in range(1, list_data.length+1):
    word = list_data.get(i)
    if(len(word) %2==1): count_odd+=1

print('Count of words with odd length:', count_odd)

# Using Arrays
array_data = input_data[:-1].split(' ')

alphabet_array = []
alpha_word=''
for i in range(97, 122): 
    alpha_word += chr(i)
    alphabet_array.append(alpha_word)
    
def is_consisted(word, words):
    for i in words:
        if(word == i):
            return True
    return False
result_array = []
for word in array_data:
    if(is_consisted(word, alphabet_array) and word!=array_data[0]):
        result_array.append(word)

print('\nAlphabetical words which do not coincide with the first:', result_array)

count_odd = 0
for word in array_data:
    if(len(word) %2==1): count_odd+=1

print('Count of words with odd length:', count_odd)