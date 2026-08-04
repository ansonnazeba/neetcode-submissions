class Solution {
public:
    bool isHappy(int n) {
        std::unordered_set<int> nums;
        int sum = 0;

        while (1) {
            for (auto c: std::to_string(n)) {
                sum += std::pow(c - '0', 2);
            }

            std::cout << std::to_string(sum) << '\n';

            if (sum == 1)
                return true;
            if (nums.contains(sum))
                return false;

            nums.insert(sum);
            n = sum;
            sum = 0;
        }

        return false;
    }
};
