class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number = {}
        for num in nums:
            number[num] = number.get(num, 0) + 1

        number = sorted(number.items(), key=lambda x : x[1],reverse = True)

        array = []
        for i in range(k):
            array.append(number[i][0])
        return array