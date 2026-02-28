class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        s = num1.replace("i", "j").replace("+-", "-")
        s1 = num2.replace("i", "j").replace("+-", "-")

        c1=complex(s)
        c2=complex(s1)
        c=c1*c2
        real = int(c.real)
        imag = int(c.imag)
        
        return str(real) + "+" + str(imag) + "i"
        