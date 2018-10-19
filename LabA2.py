#Raul Rodriguez
#80549657
#10-18-18


class Node(object): #Node class
    item = -1
    next = None
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

def Repeat(x): #Find duplicates
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
                
    return repeated
           
def nestedLoops(mergeLists,size):  #O(n^2) ,Nested Loops
    print("Nested Loops =", end = ' ')
    for i in range(0, size):
        for j in range(i+1, size):
            if mergeLists[i]==mergeLists[j]:
                print(mergeLists[i], end = ' ')
            
                
def bubbleSort(mergeLists):  #O(n^2)  , Bubble Sort
    for i in range(len(mergeLists)-1,0,-1):
        for j in range(i):
            if mergeLists[j]>mergeLists[j+1]:
                temp = mergeLists[j]
                mergeLists[j]=mergeLists[j+1]
                mergeLists[j+1]=temp
                
def mergeSort(mergeLists):  #O(n log(n))  , Merge Sort
    if len(mergeLists)>1:
        mid = len(mergeLists)//2 #divies list by two
        lefthalf = mergeLists[:mid]
        righthalf = mergeLists[mid:]

        mergeSort(lefthalf) #recursive calls
        mergeSort(righthalf)

        i=j=k=0
    
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
               mergeLists[k]=lefthalf[i]
               i=i+1
            else:
                mergeLists[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            mergeLists[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            mergeLists[k]=righthalf[j]
            j=j+1
            k=k+1
            
            

def rangeBoolean(mergeLists,m): # O(n^2) , Range of m+1
    seen = [False]*(m+1) #Create a list of false 
    for i in range (0, len(mergeLists)-1): #loop to find if element if duplicated
        for j in range(i+1,len(mergeLists)):
            if mergeLists[i]==mergeLists[j]: #if duplicated
                seen[mergeLists[i]] == True 
                break
    for i in range(m+1):
        if seen[i]==True:
              return True
    return False    

                                          
if __name__ =='__main__':
    with open('vivendi.txt', 'r') as myfile: #calls on vivendi.txt file
        vivendi = []
        for line in myfile: vivendi.append(int(line.strip()))
        #print(vivendi)


    with open('activision.txt', 'r') as myfile:  #calls on activision.txt file
        activision = []
        for line in myfile: activision.append(int(line))      
        #print(activision)               

import time
start_time = time.time()
new_list = activision + vivendi
bubbleSort(new_list)
print('Bubble Sort =', Repeat(new_list))
new_list.sort()
mer_size = len(new_list)
nestedLoops(new_list, mer_size)
print()
mergeSort(new_list)
print('Merge Sort =', Repeat(new_list))
print('Boolean Array =', rangeBoolean(new_list, 1000))
print("%s seconds"% (time.time() - start_time))
