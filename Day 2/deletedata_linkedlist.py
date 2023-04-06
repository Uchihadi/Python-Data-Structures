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
        temp = self.__head
        while (temp is not None):
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None                                               
        #Remove pass and copy the code you had written to find the node containing the element.

    
    def insert(self,data,data_before):
        pass
        #Remove pass and copy the code you had written to insert an element.
    
    def delete(self,data):
        node = self.find_node(data)
        if (node is not None):
            if (node == self.__head):
                if(self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while (temp is not None):
                    if(temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if (node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked List")
        #Remove pass and write the logic to delete an element.
                                              
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
#Delete the required element.
list1.delete("Sugar")
list1.display()
                                              