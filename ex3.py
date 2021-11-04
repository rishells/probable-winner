# This is very similar code to the above example, but now the inner for loop starts at i + 1.

# void printUnorderedPairs(int[] array) {
#     for (int i= 0; i < array.length; i++) {
#         for (int j = i + 1; j < array.length; j++) {
#             System.out.println(array[i] + "," + array[j]);
#         }
#     }
# }

arr = [1,2,3,4,5]
def printUnorderedPairs(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"{arr[i]} , {arr[j]}")

printUnorderedPairs(arr)
print(len(arr))