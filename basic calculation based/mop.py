'''def validity(ls: list) -> bool:
    'matrix validity func'
    if isinstance(ls[0], list):  # Check if the first element is a list
        ln = len(ls[0])  # Get the length of the first row
        for i in ls:  # Iterate over all rows in the matrix
            if not isinstance(i, list) or len(i) != ln:  # Check if each row is a list and has the same length as the first row
                return False
        return True
    return False
def size(ls: list) -> tuple:
    return len(ls), len(ls[0])
# Matrix operations
m1 = [[1, 2], [3, 4], [6, 9]]
m2 = [[1, 5], [9, 4], [9, 9]]
# 3 rows and 2 columns
def size(ls:list)->list:
    return len(ls),len(ls[0])
m1=[[1,2],[3,4],[6,9]]
m2=[[10,0],[0,9],[1,1]]
if validity(m1) and validity(m2):
    r1,c1=size(m1)
    r2,c2=size(m2)
    if (r1,c1) == (r2,c2):
        m=[[0]*c1]*r1
        for i in range(r1):
            for j in range(c1):
                m[i][j]=m1[i][j]+m2[i][j]
else:
    print('matrix is not valid')'''


    # syllabus 
    # set dictionary function 
    # scope of variable 
    # string
    # list 
    # scope of local scope within function only 
    # type of scope in namee  unbound local error 
    # any varriaable taken as an value an we assign somthin else then we get unbound local error 
    # local does not have any power to change vaue for global scope 
    # non local - locaal function havin nested scope only in py only nested function 
    
'''def add():
        def func1():
            ab=20
        def func2():
            ab=0
        def func3():
            ab=400
        ab=100
        func1()
        print(ab)
        func2()
        print(ab)
        func3()
        print(ab)
ab=10
add()
print(add)'''
# types of arguements 
def add(a,b,**c):  # because of c it will return in a dictionary c part  what if u give single to y 
     return a+b    # single k liye tuple mei and doble astrid mei dictionary 
x=10
y=120
out=add(x,y,c=34) # if u add extra it will raise a type error
print(out)
# keyword and positional arguement 
marks={'ravi':10,'xyz':20,'abc':40}
print(marks['xyz'])

def apna_fun(x):
     return x+2
ls=[10,20,30]
out=list(map(apna_fun,ls)) # map filter 
print(out)    

def trans(x):
     return x%2==0 
ls=[110,203,304]
out=list(map(trans,ls)) # map filter 
print(out) 

def trans1(x):
     return x%2==0
ls=[110,203,304]
out=list(filter(trans1,ls)) # map filter 
print(out) 

# lamda function - fn without a fn name 
# lamda is a keyword 
def add(a,b):
     return a+b
out=add(2,4)
print(out)


# celcius to fahrenheit
ls=[110,203,304]
out=filter(lambda x:x%2==0,ls)
print(list(out))

name=['tanush','bn','ty','hdwb']
# names based on lexographical order 
name.sort()
print(name)
# based on length , last chr of str n askii 
name.sort(key=lambda x:x[-1])
print(name)

# askii weight 
st='tanush'
ls=[]
for i in st:
     ls.append(ord(i))
print(sum(ls))

st='tan'
name.sort(key=lambda st:sum([ord(i) for i in st]))
print(name)

