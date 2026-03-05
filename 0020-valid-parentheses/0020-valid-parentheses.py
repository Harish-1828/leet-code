class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        b=['(','[','{']
        d={'(':')','[':']','{':'}'}
        for i in s:
            if i in b:
                stack.append(i)
            else:
                if stack:
                    e=stack[-1]
                    if d[e]==i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False

        