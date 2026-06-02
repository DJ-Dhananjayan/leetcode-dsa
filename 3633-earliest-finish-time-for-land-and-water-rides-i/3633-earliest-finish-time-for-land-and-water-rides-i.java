class Solution {
    public int earliestFinishTime(int[] ls, int[] ld, int[] ws, int[] wd) {
        int a = tot(ls,ld,ws,wd);
        int b= tot(ws,wd,ls,ld);
        return Math.min(a,b);
    }


public int tot(int[] ls, int[] ld, int[] ws, int[] wd) {
int tot=0;
        int min=Integer.MAX_VALUE;
        for (int i =0;i<ls.length;i++){
            int val=ls[i]+ld[i];
            min = Math.min(min,val);
        }
        tot+=min;
        int m=Integer.MAX_VALUE;
        for (int i =0;i<ws.length;i++){
            
            m =Math.min(m,Math.max(tot,ws[i])+wd[i]);
        }
        
        return m;
}
}