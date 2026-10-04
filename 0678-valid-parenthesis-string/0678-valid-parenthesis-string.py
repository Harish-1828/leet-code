class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def fn(st, idx):
            key = (idx, len(st))
            if key in dp:
                return dp[key]
            if len(st) == 0 and idx >= len(s):
                dp[key] = True
                return True
            if st and idx >= len(s):
                dp[key] = False
                return False
            else:
                if s[idx] == "*":
                    if fn(st, idx + 1):
                        dp[key] = True
                        return True
                    st.append('(')
                    if fn(st, idx + 1):
                        dp[key] = True
                        return True
                    st.pop()
                    if st:
                        st.pop()
                        if fn(st, idx + 1):
                            dp[key] = True
                            return True
                        else:
                            st.append('(')
                            dp[key] = False
                            return False
                    dp[key] = False
                    return False
                else:
                    if s[idx] == '(':
                        st.append('(')
                        if fn(st, idx + 1):
                            dp[key] = True
                            return True
                        else:
                            if st:
                                st.pop()
                            dp[key] = False
                            return False
                    else:
                        if st:
                            st.pop()
                            if fn(st, idx + 1):
                                dp[key] = True
                                return True
                            else:
                                st.append('(')
                                dp[key] = False
                                return False
                        else:
                            dp[key] = False
                            return False
                dp[key] = False
                return False
        return fn([], 0)