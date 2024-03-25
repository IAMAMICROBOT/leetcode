class Solution {
    public int alternateDigitSum(int n) {
        int res=0;
        String num=Integer.toString(n);
        int len=num.length();
        for(int i=0;i<len;i++){
            if(i%2==0)
                res += Character.getNumericValue(num.charAt(i));
            else
                res -= Character.getNumericValue(num.charAt(i));


        }
        return res;
    }
}
