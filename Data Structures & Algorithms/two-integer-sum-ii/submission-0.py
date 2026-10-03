class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indize = [0] * 2
        j = len(numbers) -1
        i = 0
        while (i<j):
            if ((numbers[i] +  numbers[j]) == target):
                indize[0] = i + 1
                indize[1] = j + 1
                return indize
            elif ((numbers[i] +  numbers[j]) > target):
                j -= 1
            else:
                i += 1

