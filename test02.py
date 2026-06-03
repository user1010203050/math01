S=0
F=0
for n in range(1,50,1):
    S=S+(2*n+1)/(n*(n+1)*(2*n+1))**3
    F=(9486-93*S)**.5
    print("pi_",n,"=",F/31)                
                 
