class Solution:
    def isValid(self, s: str) -> bool:
        paren_set = {"]" : "[",
                    ")" : "(",
                    "}" : "{"}
        st = []

        for _ in s:
            if _ in paren_set and len(st) >= 1:
                x = st.pop() == paren_set.get(_)
                if not x:
                    return False
            else:
                st.append(_)
        
        return len(st) == 0


        