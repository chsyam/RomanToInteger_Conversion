def RomToInt(i,sum,d,s):
    if i==-1:
        return sum+d[s[i+1]]
    if i<0:
        return sum
    if d[s[i]]>=d[s[i+1]]:
        sum+=d[s[i+1]]
        return RomToInt(i-1,sum,d,s)
    else:
        sum+=d[s[i+1]]
        sum-=d[s[i]]
        return RomToInt(i-2,sum,d,s)
s = input()
d={}
d['I']=1
d['V']=5
d['X']=10
d['L']=50
d['C']=100
d['D']=500
d['M']=1000
if(len(s)==1):
    print(d[s[0]])
else:
    sum=0
    n = len(s)
    print(RomToInt(n-2,sum,d,s))