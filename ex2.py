# What is the runtime of the below code?

# 1 void printPairs(int[] array) {
# 2     for (int i= 0; i < array.length; i++) {
# 3         for (int j = 0; j < array.length; j++) {
# 4             System.out.println(array[i] + "," + array[j]);
# 5         }
# 6     }
# 7 }

arr = [1,2,3,4,5]
def printPairs(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            print(f"{arr[i]} , {arr[j]}")


printPairs(arr)

# The inner loop has O(N) iterations and it is called N times. Therefore, the runtime is O(N^2)