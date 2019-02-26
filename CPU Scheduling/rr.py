n=int(input("Enter total no. of processes: "))
tq=int(input("Enter Time Quantum: "))
bt=[None] * n
p=[None]*n
for i in range(n):
    bt[i]=int(input("Enter B.T for p["+str(i)+"]: "))


def rr(bt):
    rem_bt=[None] * n
    at=[None] * n
    ct=[None] * n
    t=0

    for i in range(n):
        at[i]=int(input("Enter A.T for p["+str(i)+"]: "))
    
    for i in range(int(n)):
        for j in range(int(n)):
            if(at[i] < at[j]):
                at[i],at[j] = at[j],at[i]
                bt[i],bt[j] = bt[j],bt[i]
    rem_bt=bt
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    print("Gantt chart is as follows:")
    while(True):
        flag=False
        done=True
        for i in range(n):
                if rem_bt[i] > 0:
                    if t >= at[i]:
                        done=False
                        if rem_bt[i] > tq:
                            t=t+tq
                            print(str(t)+"|")
                            rem_bt[i]-=tq
                        else:
                            t=t+rem_bt[i]
                            flag=False
                            print("|"+str(t))
                            ct[i]=t
                            rem_bt[i]=0
                            
                    else:
                        if flag== True:
                            t+=1
                
        if done == True:
            break
    print(ct)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    



    
def priority(bt):
    temp_bt=bt
    pr=[0] * len(bt)
    for i in range(len(pr)):
        pr[i]=int(input("Enter Priority of P["+str(i)+"]: "))
    for x in range(len(pr)):
        for y in range(len(pr)):
            if(pr[x] < pr[y]):
                pr[x],pr[y]=pr[y],pr[x]
                temp_bt[x],temp_bt[y] = temp_bt[y],temp_bt[x]            
    sjf(temp_bt)
    

def fcfs(bt):
    ct=[None] * n
    tat=[None] * n
    wt=[None] * n
    at=[0] * n

    ct[0]=bt[0]
    for i in range(1,n):
        for j in range(i):
            ct[i]=ct[j]+bt[i]
    for i in range(n):
        tat[i]=ct[i]-at[i]
        wt[i]=tat[i]-bt[i]
        
    print("processes | BT | AT | CT | TAT | WT")    
    for i in range(n):
        print("p["+str(i)+"] | "+str(bt[i])+" | "+str(at[i])+" | "+str(ct[i])+" | "+str(tat[i])+" | "+str(wt[i]))

def sjf(bt):
    fcfs(sorted(bt))


    

    
