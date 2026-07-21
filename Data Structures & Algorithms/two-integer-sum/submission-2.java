class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];

            if (map.containsKey(comp)) {
                int[] inds = {map.get(comp), i};
                return inds;
            }

            map.put(nums[i], i);
            System.out.println(map);
        }

        return new int[0];
    }
}
