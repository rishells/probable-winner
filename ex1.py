# What is the runtime of the below code?
arr = [1,2,3,4,5]

def foo(arr):
    sum = 0
    product = 1
    for i in range (0,len(arr)):
        sum += arr[i]
    for i in range(0,len(arr)):
        product *= arr[i]
    print(f"{sum} , {product}")

foo(arr)

# This will take O(N) time. The fact that we iterate though the array  twice doesn't matter