class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False
        
        lower = upper = digit = special = False
        special_chars = "!@#$%^&*()-+"
        
        for i in range(len(password)):
            
            if password[i].islower():
                lower = True
            
            if password[i].isupper():
                upper = True
            
            if password[i].isdigit():
                digit = True
            
            if password[i] in special_chars:
                special = True
            
            if i > 0 and password[i] == password[i-1]:
                return False
        
        return lower and upper and digit and special