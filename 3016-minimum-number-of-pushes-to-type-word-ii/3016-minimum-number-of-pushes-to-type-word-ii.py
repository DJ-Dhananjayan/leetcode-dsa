from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        count = sorted(freq.values(), reverse=True)

        ans = 0

        for i, c in enumerate(count):
            p = i // 8 + 1
            ans += c * p

        return ans