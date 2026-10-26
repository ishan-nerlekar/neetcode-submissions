class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_joined = ''.join([c for c in s if c.isalnum()]).lower()
        i,j = 0,len(s_joined)-1

        while(i<j):
            if s_joined[i]!=s_joined[j]:
                print (f'{i}:{s_joined[i]},{j}:{s_joined[j]}')
                return False
            i,j=i+1,j-1
        return True