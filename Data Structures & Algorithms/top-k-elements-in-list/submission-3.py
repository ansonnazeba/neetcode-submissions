
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate through the array getting the number of occurences
        # build a heap of the ocurrences, that sorts the keys based on occurences
        # pop the first k occurences
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        keys_list = list(freq_map.keys())
        
        freq_list = [[] for i in range(len(nums) + 1)]
        print(freq_list)

        for key in keys_list:
            ind = freq_map[key]
            freq_list[ind].append(key)
        print(freq_list)


        list_out = []
        for i in range(len(freq_list) - 1, 0, -1):
            for val in freq_list[i]:
                list_out.append(val)
                if len(list_out) == k:
                    return list_out










            


            





        





            



        