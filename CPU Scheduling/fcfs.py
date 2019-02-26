
n=int(input("Enter total no. of Processes: "))
bt=[None]*n
p=[None]*n
for i in range(n):
    bt[i]=int(input("Enter e.t for p["+str(i)+"]: "))
    p[i]=int(input("Enter priority for p["+str(i)+"]: "))


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

def priority(bt,pt):
    for i in range(n):
        for j in range(i):
            if(pt[i]>pt[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
    
