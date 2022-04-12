for a in range(2,101):
    for b in range(2,a):
        if a%b ==0:
            break
    else:
         print(a,end=",")
         
        
