def fast_exp(x, e, mod, y):
    print("Starting values are: x-", x, ", e-", e, ", y-", y,", mod-",mod,"")
    while(e>0):
        if(e%2==0):
            e=e/2
            x=x**2%mod
        else:
            e=e-1
            y=(x*y) % mod
        print("Current values are: x-", x, ", e-", e, ", y-", y,",mod-",mod,"")
    print ("Final results are: x-",x,", e-",e,", y-",y,"")
fast_exp(5,500,56,1)
