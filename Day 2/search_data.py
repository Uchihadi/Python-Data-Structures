class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
        
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data = data
        
    def get_next(self):
        return self.__next
    
    def set_next(self,next):
        self.__next = next

#first node is known as the head
#last node is known as the tail
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        #creating empty linked list with head=tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    #appending node to the list
    def add(self,data):
        new_node = Node(data)  #creating node
        #Check if list is empty means if head is None
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            #if list is not empty
            self.__tail.set_next(new_node)
            self.__tail = new_node    #setting tail of LL as the new_node
    
    def display(self):
        if self.__head is None:
            print("Linked list is empty")
            return
        temp = self.__head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()
            
    def find(self,data):
        if self.__head is None:
            print("List is empty!!")
            return False, None
        temp = self.__head # temp is a reference to the head node
        pos = 0
        while temp is not None:
            #if true, it means list is not empty
            if temp.get_data() == data: #if data is present at head node in 1st iteration
                return True,pos
            else:
                temp = temp.get_next() #now temp will point to next node 
                pos += 1           
        return False, None
    
list1 = LinkedList()
list1.add("Sugar")
list1.add("Tea Bags")
list1.add("Milk")
list1.add("Biscuit")
print("Elements added successfully")
list1.display()

found, pos = list1.find("XYZ")
if(found):
    print("Element found at index ",pos)
else:
    print("Not found")
    
list2 = LinkedList()

found, pos = list2.find("XYZ")
if(found):
    print("Element found at index ",pos)
else:
    print("Not found")