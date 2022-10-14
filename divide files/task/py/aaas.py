a=list(map(int,input().split()))
b=list(map(int,input().split()))
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in b:
    if i in dic:
        dic[i]-=1
    else:
        print(0)
        break
else:
    print(not any(dic.values()))



