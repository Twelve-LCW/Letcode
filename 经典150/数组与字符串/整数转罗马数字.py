class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res=[]
        n=len(values)
        for i in range(n):
            value=values[i]
            symbol=symbols[i]
            while num>=value:
                num-=value
                res.append(symbol)
            if num==0:
                break
        return ''.join(res)