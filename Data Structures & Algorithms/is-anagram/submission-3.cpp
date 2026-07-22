class Solution {
public:
    bool isAnagram(string s, string t) {
        // loop through strings, and form a frequency map
        // comapre the frequency maps
        if (s.size() != t.size()) return false;
        
        unordered_map<char, int> s_map, t_map;

        for (auto st: s) {
            s_map[st] += 1;
        }

        for (auto st: t) {
            t_map[st] += 1;
        }

        // for (auto st: s) {
        //     if (s_map[st] != t_map[st]){
        //         return false;
        //     }
        // }
        return s_map == t_map;
    }
};
