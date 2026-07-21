#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            int comp = target - nums.at(i);

            if (map.contains(comp)) {
                return std::vector<int> {map[comp], i};
            }

            map[nums.at(i)] = i;
        }

        return std::vector<int> {};
    }
};
