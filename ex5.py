# Example 5
# What about this strange bit of code?
# void printUnorderedPairs(int[] arrayA, int[] arrayB) {
#     for (int i= 0; i < arrayA.length; i++) {
#         for (int j = 0; j < arrayB.length; j++) {
#             for (int k = 0; k < 100000; k++) {
#                 System.out.println(arrayA[i] + "," + arrayB[j]);
#             }
#         }
#     }
# }        

arrayA = [29,31,1,2,3,4,5]
arrayB = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def printUnorderedPairs(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            k = 0
            for k in range(k < 100000):
                print(f"{arr1[i]} , {arr2[j]}")


printUnorderedPairs(arrayA, arrayB)

#Runtime is O(ab) since 100,000 units of work is still constant