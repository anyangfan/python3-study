def foo(x,y,z,m=0,n=0):
    print(x,y,z,m,n)

def call_foo(*args,**kwargs):
    print(args,kwargs)
    foo(*args,**kwargs)

call_foo(1,2,3,m=4,n=5)