class Solution {
    public int majorityElement(int[] nums) {
        int maj=0;int res=0;
        for(int i=0;i<nums.length;i++){
            if(maj==0)
                res=nums[i];
            if(nums[i]==res)
                maj++;
            else
                maj--;
        }
        return(res);
    }
}
