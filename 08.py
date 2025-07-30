#Check if string is palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
		# code here
        rev = s[::-1]
        if s == rev:
            return True
        else:
    		    return False