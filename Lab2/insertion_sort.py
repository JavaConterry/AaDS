comparisons, swaps = 0, 0

def insertion_sort(arr, return_complexcity = False):
    global comparisons, swaps
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        
        comparisons += 1
        while j >= 0 and key < arr[j]: # shifting the array
            comparisons += 1
            swaps += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        swaps += 1

    if(return_complexcity):
        return arr, comparisons, swaps
    else:
        return arr

def independent_start():
    input_array = [i for i in input().split(' ')]
    print(insertion_sort(input_array))