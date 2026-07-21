class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0;
        int j = heights.size() - 1;
        int max_area = -1;

        while (i < j) {
            int height = std::min(heights[i], heights[j]);
            max_area = std::max(max_area, height * (j - i));

            if (heights[i] > heights[j])
                j--;
            else
                i++;
        }

        return max_area;
    }
};
