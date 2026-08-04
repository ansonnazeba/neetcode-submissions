class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        int last_sum = digits[n] + 1;
        int carry = last_sum >= 10;
        digits[n] = (last_sum) % 10;

        for (int i = n - 1; i >= 0; i--) {
            int realSum = digits[i] + carry;
            digits[i] = (realSum) % 10;
            carry = realSum >= 10;
        }

        if (carry)
            digits.insert(digits.begin(), carry);

        return digits;
    }
};
