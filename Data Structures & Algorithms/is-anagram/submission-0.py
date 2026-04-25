class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1 = dict()
        map_2 = dict()

        for i in s:
            map_1[i] = map_1.get(i, 0) + 1
        
        for i in t:
            map_2[i] = map_2.get(i, 0) + 1
        
        return map_1 == map_2

