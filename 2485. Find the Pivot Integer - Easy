class Solution {
    public int pivotInteger(int n) {
        int t_sum=0;
        int c_sum=0;
        for(int i=1;i<n+1;i++)
            t_sum+=i;
        for(int i=1;i<n+1;i++){
            c_sum+=i;
            if(c_sum*2 == t_sum+i){
                return i;
            }
        }
        return -1;

    }
}
