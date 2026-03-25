class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = { '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        path,res=[],[]
        def back(index):
            if len(path)==len(digits):
                res.append("".join(path[:]))
                return
            else:
                for i in d[digits[index]]:
                    path.append(i)
                    back(index+1)
                    path.pop()
        back(0)
        return res