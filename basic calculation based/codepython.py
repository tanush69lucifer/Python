# nested list or matrix (2d array) inout from user
'''
23  size be given disctribute the array by column n row 
123   3 inputs read row n column 
456
'''
'''r,c=list(map(int,input().split()))
H=[]
for i in range(r):
    lst=list(map(int,input().split()))
    H.append(lst)
for i in H:
    print(*i,sep='\t')

# or 
r, c = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(r)]
for row in H:
    print(*row, sep='\t')'''
# astrid or (*) is used to hold positional values 
# print k andr values ko 
print("hello\tworld ")
# why \t gives so much space ? 
# jitni data diplay hota har tab ka space h indendtation is 4
# but it is always 8 by default  all stream is divided to 8 slot
# it fullfils slot of 8 
print("hel\tworld ") # 5 spaces because it needs to fullfill the slot 
ls1=[[2,4,3],[4,5,6],[7,8,9]]
print(ls1)
for i in ls1:
    for j in i:
        print(j,end='\t') # print(*i,sep="\t") if more than 8 add one more \t
    print()
        
r,c=list(map(int,input().split()))
H1=[]
for i in range(r):
    lst=list(map(int,input().split()))
    H.append(lst)
for i in H1:
    print(*i,sep='\t')
    r,c=list(map(int,input().split()))
H2=[]
for i in range(r):
    lst=list(map(int,input().split()))
    H2.append(lst)
for i in H2:
    print(*i,sep='\t')
# if input is varying then number of lines should vary
