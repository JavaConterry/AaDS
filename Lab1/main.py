print('Program checking if a vector has an ariphmetic progression')
print('Input throught the program code: Vector of integer values')
print('Output: value, if the vector has ariphmetic progression, it`s difference will be returned\n      inf, if the are no ar. progression')


arr = [i for i in range(1, 20, 3)]
arr[3] = 5
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

print('Difference in the ariphmetic progression:', p(0))



# n=3

# stack1, stack2, stack3 = [i for i in range(1, n+1)], [], []

# def hannoy(stack1, stack2, stack3, n):
#     tower_m = stack1[:n-1]
#     if(stack1 == []):
#         return stack1
#     stack1 = stack1[n-1]
    
#     stack2.extend(hannoy(tower_m, stack2, stack3, n-1))
#     stack3.append(stack1)
#     stack1 = []
#     stack3.extend(stack2[:n-1])
#     stack2 = stack2[n-1:]
    
#     print(stack1)
#     print(stack2)
#     print(stack3)

#     res1 = stack1
#     stack1 = stack3
#     stack3 = res1

#     return stack1



# print(hannoy(stack1, stack2, stack3, n))

