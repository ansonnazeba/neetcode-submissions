class Solution {
public:
    double myPow(double x, int n) {
        double out = n >= 0? x: 1/x;
        
        if (n == 0) {
            return 1;

        } else if (n >= 1) {
            n--;
            while (n) {
                out *= x;
                n--;
            }

        } else {
            n++;
            while (n) {
                out *= 1 / x;
                n++;
            }
        }

        return out;
    }
};
