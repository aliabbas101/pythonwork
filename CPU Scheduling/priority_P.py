n=int(input("Enter total number of processes: "))
bt=[0] *n 
rem_bt=[0] * n
pt=[0] * n
at=[0] * n
terminated=[False] * n
rq=[]

mtime=0
pcount=0
for i in range(n):
    bt[i]=int(input("\n\nEnter BT["+str(i)+"]: "))
    pt[i]=int(input("Enter Priority["+str(i)+"]: "))
    at[i]=int(input("Enter AT["+str(i)+"]: "))
rem_bt=bt

while(False in terminated):

    for i in range(n):
        if(at[i] >=mtime):
            if(terminated[i] == False):
                rq.append(i)
    for i in range(len(rq)):
        max_i=rq.index(max(rq))
        
    mtime+=1
