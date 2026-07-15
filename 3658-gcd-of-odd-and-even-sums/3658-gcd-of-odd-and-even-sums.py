class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        arr=sum([2 * i + 1 for i in range(n)])
        arr2=sum([2*i for i in range(1,n+1)])
        return math.gcd(arr,arr2)