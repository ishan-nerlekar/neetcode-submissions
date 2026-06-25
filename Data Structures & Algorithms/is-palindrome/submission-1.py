class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        reversed_s=''.join(reversed(cleaned_s))
        print(cleaned_s)
        print(reversed_s)
        return reversed_s==cleaned_s
        