# array to mat 
'''
3 4 total 12 elements use two inputs only to make first line 2 vales row n column 
234567891345 '''
r,c=list(map(int,input().split()))
raw_list=list(map(int,input().split()))
M=[] # empty list
count=0
for i in raw_list:
    tmp=[]
    tmp.append(i)
    if count==c:
        M.append(tmp)
        tmp=[]
        count=0
    count+=1
    for i  in M:
        print(*i,sep='\t')