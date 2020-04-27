def prime(n):
    n=int(n)
    for i in range(2,n//2):
        if n%i==0:
            return("non prime")
            break
    else:
        return("prime")
