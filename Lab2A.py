#Raul Rodriguez
#80549657
#10-18-18


from timeit import default_timer as timer

class Node(object): #Node class
    item = -1
    next = None

    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def has_next(self):
        return self.next!=None
    def get_next(self):
        return self.next
    def set_next(self,node):
        self.next=node

class LinkedList(object): #LinkedList class
 
    def __init__(self):
        self.item=None
        self.size=0

    def length(self):
        curr = self
        total = 0
        while curr.get_next() is not None:
            total +=1
            curr = curr.get_next()
        return total
    
    def get_next(self):
        return self.item.get_next()   
  
    def add(self, item): #add new node
        new_node = Node(item, self.item);
        self.item = new_node;
        self.size += 1;
         

    def print_list(self): #print list
        print("List = ", end= "");
        if self.item is None:
            return;
        current = self.item;
        print(current.item, end=", ");
        while current.get_next():
            current = current.get_next();
            if not current.has_next():
                print(current.item, end="");
            else:
                print(current.item, end= ", ")
                                 
     

def duplicates_unsorted(self): #find duplicates in an unsorted array
    k = self.item
    duplicate_elements = []
    while k is not None:
       j = k.get_next()
       while j is not None:
           if k.item == j.item:
                duplicate_elements.append(k.item)
           j = j.get_next()
       k = k.get_next()
    print("Duplicates: ", duplicate_elements)


def duplicates_sorted(self): #find duplicates in a sorted array
    k = self.item
    duplicate_elements = []
    while k is not None:
        if k.get_next() is None:
            break
        if k.item == k.get_next().item:
            duplicate_elements.append(k.item)
        k = k.get_next()
    print("Duplicates: ", duplicate_elements)
  
def bubble_sort(num): ##O(n^2)  , Bubble Sort
    for i in range(num.length()):
        m = num.item
        n = m.get_next()
        while n is not None:
            if n.item is None:
                break
            if m.item > n.item:
                swap(m, n)
            n = n.next
            m = m.get_next()


def swap(node1, node2): #swamps each node
    temp = node1.item
    node1.item = node2.item
    node2.item = temp
   
def merge_sort(linkedList): #merge sort
    if linkedList is None or linkedList.get_next() is None:
        return linkedList
    else:
        middle = get_middle(linkedList)
        nextmiddle = middle.get_next()
        middle.next = None

        left = merge_sort(middle)
        right = merge_sort(nextmiddle)

        sortedList = merge_list(left, right)

        return sortedList

def merge_list(left, right): #merge lists

    if left is None:
        return left
    elif right is None:
        return right

    if (int(right.item) <= int(left.item)):
        result = right
        result.next = merge_list(right.next, left)
        result = left
        result.next = merge_list(right, left.next)
    return result


def get_middle(linkedList): #get middle of list
    
    if linkedList is None or linkedList.get_next() is None:
        return linkedList
    else:
        fastpointer = linkedList.get_next
        slowpointer = linkedList

        while fastpointer != None:
            fastpointer = fastpointer.next
            slowpointer = slowpointer.next

        return slowpointer
  
  
def checkBoolean(linkedList): #boolan array of length m+1 O(n^2)
    seen = [False]*(linkedList.length()+1)
    m = linkedList
    n = m.get_next()
    while n is not None:
        if m.item == n.item:
            seen[m.item] = True
            m = m.get_next()
            if m == n:
                n = n.get_next()
                m = LinkedList
            return seen    

def checkBoolean_list(boolean_list): #prints duplicates from the boolean method
    duplicate_elements = []
    for i in range(len(boolean_list)):
        if boolean_list[i] == True:
            duplicate_elements.append(i)
    print("Duplicates: ", duplicate_elements) 
    

def single_list():
     merge_list = LinkedList() #create empty linked list
     with open('vivendi.txt', 'r') as myfile: #calls on vivendi.txt file
        for line in myfile:
           merge_list.add(int(line.strip()))
        myfile.close()

     with open('activision.txt', 'r') as myfile: #calls on activision.txt file
        for line in myfile:
            merge_list.add(int(line))    
        myfile.close  
     return merge_list

def main():
   
   #creating a linked list
   linkedList=single_list()
   #linkedList.print_list()
   print()
   unsorted_timer = timer()
   duplicates_unsorted(linkedList)
   unsorted_end_timer = timer()
   total_time = (unsorted_end_timer - unsorted_timer)
   print("Time for dulpicates in unsorted array: ", total_time)
   print()  
   
   bubble_sortlist = single_list()
   #bubble_sortlist.print_list()
   print()
   unsorted_timer = timer()
   bubble_sort(bubble_sortlist)
   unsorted_end_timer = timer()
   total_time = (unsorted_end_timer - unsorted_timer)
   bubble_sortlist.print_list()
   print()
   print("Time for bubble sort: ", total_time)
   print()
   unsorted_timer = timer()
   duplicates_sorted(bubble_sortlist)
   unsorted_end_timer = timer()
   total_time = (unsorted_end_timer - unsorted_timer)
   print(total_time)
   
   #merge_sortlist = single_list()
   #merge_sortlist.print_list()
   #print()
   #merge_sort(merge_sortlist)
   #merge_sortlist.print_list()
   #print()
   #duplicates_sorted(merge_sortlist) 

   #booleanList = single_list()
   #booleanList.print_list()
   #print()
   #boolean_list = checkBoolean(booleanList)
   #print(boolean_list)
   #checkBoolean_list(booleanList)

if __name__ =='__main__':
    main()