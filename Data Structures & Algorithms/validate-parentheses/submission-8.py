class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        stack = []

        for c in s:
            if c==")" or c=="]" or c=="}":
                if c==")":
                    if stack and stack[-1]!="(":
                        return False
                    else:
                        if stack:
                            stack.pop()
                        else:
                            return False
                if c=="]":
                    if stack and stack[-1]!="[":
                        return False
                    else:
                        if stack:
                            stack.pop()
                        else:
                            return False
                if c=="}":
                    if stack and stack[-1]!="{":
                        return False
                    else:
                        if stack:
                            stack.pop()
                        else:
                            return False
            else:
                stack.append(c)
        
        return not stack
