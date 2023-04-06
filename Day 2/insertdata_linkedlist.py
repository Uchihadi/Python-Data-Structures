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
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        pass
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        pass
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        pass
        #Remove pass and copy the code you had written to find the node containing the element.
    
    def insert(self,data,data_before):
        new_node = Node (data)
        if (data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if (new_node.get_next() == None):
                self.__tail = new_node
                
        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next (new_node)
                
                if (new_node.get_next() is None):
                    self.__tail = new_node
            
            else:
                print (data_before, "is not present in the Linked List")
        #Remove pass and write the logic to insert an element.
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
#Add all the required element(s)
#Insert the element in the required position
list1.insert("NewItem","Sugar")
list1.display()
                                              