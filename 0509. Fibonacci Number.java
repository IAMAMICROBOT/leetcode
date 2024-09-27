class Solution {
    public int fib(int n) {
        int[] fibb=new int[n+1];
        if(n<=1){
            return(n);
        }
        else{
            fibb[0]=1;
            fibb[1]=1;
            for(int i=2;i<n;i++){
                fibb[i]=(fibb[i-1]+fibb[i-2]);
            }
            return(fibb[n-1]);
        }
    }
}
