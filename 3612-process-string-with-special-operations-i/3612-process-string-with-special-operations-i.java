class Solution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        int i=0;
        while (i<s.length()){
            char c=s.charAt(i);
            if(c=='#'){
                int a=sb.length();
                sb.append(sb);
            }
            else if(c=='%'){
                sb.reverse();
            }
            else if(c=='*' ){
                if( sb.length()>0)
                    sb.deleteCharAt(sb.length()-1);
            }
            else {
                sb.append(c);
            }
            i++;
        }
        return (sb.toString());
    }
}