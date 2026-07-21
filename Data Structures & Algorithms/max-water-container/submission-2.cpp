class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0;
        int j = heights.size() - 1;
        int max_area = -1;

        while (i < j) {
            int height = heights[i] > heights[j]? heights[j]: heights[i];
            int area = height * (j - i);
            max_area = area > max_area? area: max_area;

            if (heights[i] > heights[j])
                j--;
            else
                i++;
        }

        return max_area;
    }
};
