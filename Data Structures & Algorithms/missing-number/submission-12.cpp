class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expectedSum = (nums.size() * (nums.size() + 1) / 2);
        
        for (auto num: nums) {
            expectedSum -= num;
        }

        return expectedSum;
    }
};
