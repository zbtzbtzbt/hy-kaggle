#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zbt
# datetime:2020-02-17 14:57
# software: PyCharm
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        for start in range(1,tsum//2 +1):
            for d in range(2,tsum):
                tmpSum=(2*start+d-1)*d
                if tmpSum==2*tsum:
                    tmp=[i for i in range(start,start+d)]
                    res.append(tmp)
                    break
        return res

def main():
    F=Solution()
    n=100
    print(F.FindContinuousSequence(n))

if __name__=='__main__':
    main()
