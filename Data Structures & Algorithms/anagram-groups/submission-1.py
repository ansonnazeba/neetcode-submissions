class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash each input
        # create a map(hash numbers as keys, strings as values)
        # return the values list

        group_map = dict()

        for _ in strs:
            count = 26 * [0]

            for ch in _:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count) # using a tople since it is immutable
            if key not in group_map:
                group_map[key] = []
            group_map[key].append(_)
        
        out_list = []
        for key in group_map:
            out_list.append(group_map.get(key))
        
        return out_list
        