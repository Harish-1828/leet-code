class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)

        if k > n:
            return []

        count = [0] * 26

        # Frequency of p
        for ch in p:
            count[ord(ch) - ord('a')] += 1

        # First window
        for i in range(k):
            count[ord(s[i]) - ord('a')] -= 1

        res = []

        # Check first window
        if all(x == 0 for x in count):
            res.append(0)

        # Slide the window
        for i in range(k, n):

            # Add new character
            count[ord(s[i]) - ord('a')] -= 1

            # Remove old character
            count[ord(s[i - k]) - ord('a')] += 1

            # Check if anagram
            if all(x == 0 for x in count):
                res.append(i - k + 1)

        return res