class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start=0;
        int end=nums.length-1;
        while(start<=end){
            if(nums[start]==target && nums[end]==target){
                return new int[]{start,end};
            }
            if(nums[start]!=target)
                start++;
            if(nums[end]!=target)
                end--;
        }
        return new int[]{-1,-1};
    }
}
