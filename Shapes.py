
def draw() :
    n=7
    s="*"
    for i in range(0,n,1):
        if i == 0 or i == n-1:
            print(s*n)
        else:
            print(s+(" "*(n-2))+s)


draw()
