input_array = [i for i in input().split(' ')]


def quick_sort(arr):
    p = arr[-1] # pivot set to be the end value
    i, j = -1, 0 # initial indecies
    while j<len(arr)-1:
        if(arr[j]<p):
            i+=1
        if(i!=-1 and arr[i]>arr[j]): # swap if two are descending
            res = arr[i] 
            arr[i] = arr[j]
            arr[j] = res
        j+=1
    i+=1
    if(arr[i]>p): # final swap if end value i and pivot are descending
        res = arr[i]
        arr[i] = p 
        arr[-1] = res
    if(len(arr)>1): # recursion of splitted arrays by i value, if those are larger then 2
        # print(arr[:i], i, arr[i+1:])  # diviation debug

        if(len(arr[:i])>1):  
            arr[:i] = quick_sort(arr[:i])
        if(len(arr[i:])>1):
            arr[i+1:] = quick_sort(arr[i+1:])
    return arr
        


print(quick_sort(input_array))