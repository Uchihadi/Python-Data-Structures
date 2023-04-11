import sys
sys.setrecursionlimit(10000) #Recursion
def code1(num):
    if(num<=2):
        return 1
    else:
        return (code1(num-1)+code1(num-2))
print(code1(10))

import sys
sys.setrecursionlimit(10000) #Memorization Technique: Store immediate value and save for another timr
def code2(num):
    global memo
    if(num<=2):
        return 1
    if(memo.get(num)!=None):
        return memo[num]
    else:
        val=code2(num-1)+code2(num-2)
        memo.update({num:val})
        return memo[num]
memo={}
print(code2(10))

import sys
sys.setrecursionlimit(10000)
def code3(num):
    global memo
    if(num<=2):
        return 1
    if(memo.get(num)!=None):
            return memo[num]
    for n in range(2,num+1):
        val=code3(n-1)+code3(n-2)
        memo.update({n:val})
    return memo[num]
memo={}
print(code3(10))