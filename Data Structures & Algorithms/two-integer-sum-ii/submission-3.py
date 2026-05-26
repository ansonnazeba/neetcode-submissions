class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # cannot use any additonal data strutures
        slow = 0
        list_out = []

        while slow < len(numbers) - 1:
            l = numbers[slow + 1:]
            complement = target - numbers[slow]
            print(complement)

            if complement in l:
                ind = l.index(complement) + slow + 2
                return [slow + 1, ind]

            slow += 1
        
        return []

        