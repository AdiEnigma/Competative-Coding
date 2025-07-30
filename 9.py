#Count frequency of array elements
class Solution:
    def countFreq(self, arr):
        freq = {}
        for x in arr:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        res = []
        for key in sorted(freq):
            res.append([key, freq[key]])

        return res
