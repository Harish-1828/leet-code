from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p=paragraph.lower().split()
        p=re.sub(r'[!?,;.\']',' ',paragraph)
        p=p.lower().split()
        f = list(filter(lambda x: x not in banned, p))
        c=Counter(f)
        return max(c,key=c.get)