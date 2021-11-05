# The following code reverses an array. What is its runtime?
# void reverse(int[] array) {
#   for (inti= 0; i <array.length/ 2; i++) {
#       int other= array.length - i - 1;
#       int temp= array[i];
#       array[i] = array[other];
#       array[other] = temp;
#   }
# }

arr = [1,2,3,4,5]

def reverse(arr):
    i = 0
    for i in range(i < len(arr)/2):
        other = len(arr) - i -1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp

reverse(arr)
print(arr)

#This algorithm runs O(N) time.