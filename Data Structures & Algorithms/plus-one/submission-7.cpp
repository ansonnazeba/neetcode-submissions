class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() - 1;
        int carry = 0;
        digits[n] += 1;

        for (int i = n; i >= 0; i--) {
            int realSum = digits[i] + carry;
            digits[i] = (realSum) % 10;
            carry = realSum >= 10;
        }

        if (carry)
            digits.insert(digits.begin(), carry);

        return digits;
    }
};
