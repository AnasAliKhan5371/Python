n=1                #global
def fn():
    n=5            #local
    print('in',n)
fn()
print('out',n)