class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        res=0 
        presses=1
        while n>=8:
            res+=(8*presses)
            presses+=1
            n-=8
        res+=(n*presses)
        return res