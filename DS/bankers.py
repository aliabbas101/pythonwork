import random
print("Enter total processes: ")
p=int(input())
print("Enter total resources: ")
r=int(input())
totalres=[0] * r
terminated=[False] * p
sequence=[]
count=0
check=0
for i in range(len(totalres)):
    totalres[i]=int(input("Enter total resources for "+str(i)+" :"))
    
col, row = r, p;


#randomly generating valid maximum need and allocation matrix and need=max-allocation

##      Max = [[random.randint(0,totalres[x]) for y in range(col)] for x in range(row)]
##      Allocation = [[random.randint(0,Max[x][y]) for y in range(col)] for x in range(row)]
##    Max = [[int(input()) for x in range(row)] for y in range(col)]
##    Allocation = [[int(input()) for x in range(row)] for y in range(col)]
Max = [[7,5,3],
       [3,2,2],
       [9,0,2],
       [4,2,2],
       [5,3,3]]
Allocation = [[0,1,0],
             [2,0,0],
             [3,0,2],
             [2,1,1],
             [0,0,2]]

Need = [[Max[x][y] - Allocation[x][y] for y in range(col)] for x in range(row)]
print("Max: ")
for eachrow in Max:
    print(eachrow)
print("Allocation: ")
for eachrow in Allocation:
    print(eachrow)
print("Need Matrix: ")
for eachrow in Need:
    print(eachrow)
#----------------------------------
ttlalloc=[0] * r
print("total Allocation: ")
for x in range(row):
    for y in range(col):
        ttlalloc[y]+=Allocation[x][y]
        
available=[totalres[i]-ttlalloc[i] for i in range(col)]
print("-------------------")
print("Available at starting : ")
print(available)

#deadlock checking
while(False in terminated):
    for x in range(row):
        if(terminated[x]== False):
            for y in range(col):
                if(available[y] >= Need[x][y]):
                    check+=1
            if(check==col):
                terminated[x]=True
                available=[available[i]+Allocation[x][i] for i in range(col)]
                sequence.append("P["+str(x)+"]")
                print(available)
                
            else:
                terminated[x]=False
            check=0
        else:
            continue
if False in terminated:
    print("The Deadlock occured")
else:
    print("The deadlock will not occur !")
    print("Here's the following Safe Sequence: ")
    print(sequence)
    print("The available after every resource was released by "+str(row)+"Processes: ")
    print(available)
    
print(terminated)
        
        

