class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = 1;
        }
        int l_prod=1;
        for(int i=0;i<n;i++){
            res[i]*=l_prod;
            l_prod*=nums[i];
        }
        int r_prod=1;
        for(int i=n-1;i>-1;i--){
            res[i]*=r_prod;
            r_prod*=nums[i];
        }
    return res;
    }
}
