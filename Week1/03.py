#Find second largest element
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        largest = arr[0]
        second_largest = -1

        for i in arr[1:]:
            if i > largest:
                second_largest = largest
                largest = i
            elif i != largest and i > second_largest:
                second_largest = i

        return second_largest


