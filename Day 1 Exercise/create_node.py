#first node is known as the head
#last node is known as the tail
# Creating a Node: Sugar
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node

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
            self.__tail.set_next(new_node) #Setting tail of linked list as a new node
            self.__tail = new_node 
            
    def display(self):
        if self.__head is None:
            print("Linked list is empty")
            return
        temp = self.__head #Make temp node as my head node
        while temp:
            print(temp.get_data())
            temp = temp.get_next() #head and tail still be same; storing head as temp to create a new chain of node
            # Run until the next value is not None
  
list1 = LinkedList()
list1.add("Sugar")
list1.add("Tea Bags")
list1.add("Milk")
list1.add("Biscuit")
print("Elements added successfully")
list1.display()