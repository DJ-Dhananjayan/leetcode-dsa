class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int i=0,res=0;
        while(i<costs.length && coins>=costs[i]){
            res++;
            coins-=costs[i++];
        }
        return res;
    }
}