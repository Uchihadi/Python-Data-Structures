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

def insert_before(self, data, data_before):
        new_node = Node(data)
        # First check if LL is empty, if so,display error msg and exit from method
        if self.__head is None:
            print("Error, List is already empty")
            return 
        
        #Check if new_node needs to be inserted before the head node
        if self.__head.get_data() == data_before:
            new_node.set_next(self.__head)
            self.__head = new_node
            return
        
        #Check if new_node needs to be inserted before other nodes except head node
        #First search for data_before 
        temp = self.__head
        while temp.get_next() is not None:
            if temp.get_next().get_data() == data_before:
                #if true
                new_node.set_next(temp.get_next())
                temp.set_next(new_node)         
            temp = temp.get_next() #move temp to point to next node