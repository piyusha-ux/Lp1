#FIFO page replacement algorithm

def FIFO():
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,fault,top,pf = [],0,0,'No'
    print("Enter the reference string: ",end="")
    s = list(map(int,input().strip().split()))
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in s:
        if i not in f:
            if len(f)<capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top+1)%capacity
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))




#Optimal page replacement algorithm (OPT or OPR)

def OPR():
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,fault,pf = [],0,'No'
    print("Enter the reference string: ",end="")
    s = list(map(int,input().strip().split()))
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    occurance = [None for i in range(capacity)]
    for i in range(len(s)):
        if s[i] not in f:
            if len(f)<capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i+1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i+1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t"%s[i],end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
   
   
   

#LRU page replacement algorithm

def LRU():
    print("Enter the number of frames: ",end="")
    capacity = int(input())
    f,st,fault,pf = [],[],0,'No'
    print("Enter the reference string: ",end="")
    s = list(map(int,input().strip().split()))
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in s:
        if i not in f:
            if len(f)<capacity:
                f.append(i)
                st.append(len(f)-1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'No'
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))






while True:
    print("\nPage Replacement Algorithms")
    print("1.FIFO")
    print("2.OPR")
    print("3.LRU")    
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("\nPage Replacement using FIFO Algorithm\n")
        FIFO()
    elif choice==2:
        print("\nPage Replacement using OPR Algorithm\n")
        OPR()
   
    elif choice==3:
        print("\nPage Replacement using LRU Algorithm\n")
        LRU()
   
    elif choice==4:
        print("\nProgram Ended Successfully :) \n")
       
        break
    else:
        print("Enter a correct choice!")