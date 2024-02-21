comparisons, swaps = 0, 0

def quick_sort(arr, return_complexcity = False):
    global comparisons, swaps
    p = arr[-1] # pivot set to be the end value
    i, j = -1, 0 # initial indecies
    while j<len(arr)-1:
        if(arr[j]<p):
            comparisons += 1
            i+=1
        if(i!=-1 and arr[i]>arr[j]): # swap if two are descending
            comparisons += 1
            swaps += 1
            # print('a')
            res = arr[i] 
            arr[i] = arr[j]
            arr[j] = res
        j+=1
    i+=1
    if(arr[i]>p): # final swap if end value i and pivot are descending
        comparisons += 1
        swaps += 1
        res = arr[i]
        arr[i] = p 
        arr[-1] = res
    if(len(arr)>1): # recursion of splitted arrays by i value, if those are larger then 2
        # print(arr[:i], i, arr[i+1:])  # diviation debug
        if(len(arr[:i])>1): 
            arr[:i] = quick_sort(arr[:i])
        if(len(arr[i:])>1):
            arr[i+1:] = quick_sort(arr[i+1:])
    if(return_complexcity):
        return arr, comparisons, swaps
    else:
        return arr
        


def independent_start():
    input_array = [i for i in input().split(' ')]
    print(quick_sort(input_array))