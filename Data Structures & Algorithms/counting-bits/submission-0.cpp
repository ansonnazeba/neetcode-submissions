class Solution {
public:
    vector<int> countBits(int n) {
        int num = 1;
        vector<int> nums;
        nums.push_back(0);

        while (num <= n) {
            std::cout << std::to_string(num) << '\n';
            int num_bits = 0;
            int num_copy = num;

            while (num_copy > 0) {
                num_bits += num_copy & 1;
                num_copy = num_copy >> 1;
            }

            num++;
            nums.push_back(num_bits);
        }

        return nums;
    }
};
