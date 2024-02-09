print('Program checking if a vector has an ariphmetic progression')
print('Input throught the program code: Vector of integer values')
print('Output: value, if the vector has ariphmetic progression, it`s difference will be returned\n      inf, if the are no ar. progression')


arr = [i for i in range(1, 20, 3)]
arr.append(5)
print('input: ', arr)


def p(i):
    a = arr[i+1] - arr[i]
    if(i>=len(arr)-2):
        return a
    c = p(i+1)
    if(a==c):
        return a
    else:
        return 'Not an ariphmetic progression'

print(p(0))