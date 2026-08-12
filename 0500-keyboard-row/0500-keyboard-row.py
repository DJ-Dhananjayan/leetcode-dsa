class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiop"
        b="asdfghjkl"
        c="zxcvbnm"
        val=[]
        for i in words:
            w=i.lower()
            if len(set(a+w))==len(a) or len(set(b+w))==len(b) or  len(set(c+w))==len(c) :
                val.append(i)
        return val