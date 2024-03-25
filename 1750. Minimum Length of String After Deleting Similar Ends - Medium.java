class Solution {
    public int minimumLength(String s) {
        int l=0;
        int r=s.length()-1;
        while(l<r){
            if(s.charAt(l)==s.charAt(r)){
                char cur=s.charAt(l);
                while(l<=r && s.charAt(l)==cur)
                    l=l+1;
                while(r>=l && s.charAt(r)==cur)
                    r=r-1;
            }
            else break;
        }
        if(0>(r-l+1)) return(0);
        else return(r-l+1);
    }
}
