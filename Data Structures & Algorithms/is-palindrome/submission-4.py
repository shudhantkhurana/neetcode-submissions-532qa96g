class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j: 
            num_i = ord(s[i].lower())
            while (not ((122 >= num_i>= 97) or (57 >=num_i>= 48))) and i<j:
                i += 1
                num_i = ord(s[i].lower())

            num_j = ord(s[j].lower())
            while (not ((122 >=num_j>= 97) or (57 >=num_j>= 48))) and i<j:
                j -= 1
                num_j = ord(s[j].lower())
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1


        return True