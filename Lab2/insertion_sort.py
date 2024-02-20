input_array = [i for i in input().split(' ')]

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        while j >= 0 and key < arr[j]: # shifting the array
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort(input_array))