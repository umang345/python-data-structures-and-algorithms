class Solution:
    def countAndSay(self, n: int) -> str:
        if n<1:
            raise Exception("Invalid Input to countAndSay() -> "+n)
        if n==1:
            return "1"
        encodedStr = self.countAndSay(n-1)

        result = []
        start,end = 0,0
        while end < len(encodedStr):
            if encodedStr[start]!=encodedStr[end]:
                currLen = end-start
                result.append(f"{currLen}{encodedStr[start]}")
                start=end
            
            end+=1
        
        currLen = end-start
        result.append(f"{currLen}{encodedStr[start]}")
        return "".join(result)