class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lstrip()
        sign=1
        i=0
        if len(s)==0:
            return 0
        if s[i]=="-":
            sign=-1
            i+=1
        elif s[i]=="+":
            i+=1
        res=0
        while i<len(s) and s[i].isdigit():
            res=res*10+int(s[i])
            i+=1
        res*=sign

        int_min=-2**31
        int_max=2**31-1
        if res<int_min:
            return int_min
        if res>int_max:
            return int_max
        return res