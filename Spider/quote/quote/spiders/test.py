

def createGenerator():
    mylist = range(3)
    gen=(x*x for x in range(1,4))
    gen2=[x*x for x in range(1,4)]
    print(list(gen)*2)
    print(list(gen))
    # print(list(gen2))
    # print(list(gen2))
    # print(gen)
    print(list(mylist))
    for i in mylist:
        print(i)
        yield{ print(i*i) }
        
def fab(max): 
    n, a, b = 0, 0, 1 
    l=[]
    while n < max: 
        # print(b)
        l.append(b)
        a, b = b, a + b 
        n = n + 1
    return l



createGenerator()
print(fab(5))

grid=100
line="tes"
print(line.center(grid))

def foo(a,item=[]):
    if not item==None:
        item=[]
    item.append(a)
    return item
print(foo(1))
print(foo(2))

def fooo(a,item=None):
    # if item==None:
        # item=[]
    item.append(a)
    return item
print (fooo(2))
print (fooo("fdsfd"))