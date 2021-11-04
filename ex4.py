# This is similar to the above, but now we have two different arrays.
# void printUnorderedPairs(int[] arrayA, int[] arrayB) {
#     for (inti= 0; i < arrayA.length; i++) {
#         for (int j = 0; j < arrayB.length; j++) {
#             if (arrayA[i] < arrayB[j]) {
#                 System.out.println(arrayA[i] + "," + arrayB[j]);
#             }
#         }
#     }
# }

arrayA = [29,31,1,2,3,4,5]
arrayB = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def printUnorderedPairs(arrayA,arrayB):
    printer_counter = 0
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(f"{arrayA[i]} , {arrayB[j]}")
                printer_counter +=1
                print(printer_counter)

printUnorderedPairs(arrayA, arrayB)


# This is going to have a runtime of O(ab) not O(N^2) because the IF estatement within j's loop is O(1) time since it's just a sequence of contant-time statements
