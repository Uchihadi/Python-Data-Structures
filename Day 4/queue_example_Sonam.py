class Queue:
    def __init__(self,max_size):
       self.__max_size=max_size
       self.__elements=[None]*self.__max_size
       self.__front=0
       self.__rear=-1
       
    def is_empty(self):
        if (self.__front>self.__rear):
           return True
        return False
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
           return True
        return False
        
    def enqueue(self,data):
        if(self.is_full()):
           print ("Queue is full")
        else:
           self.__rear+=1    
           self.__elements[self.__rear]=data
           
    def dequeue(self):
        if (self.is_empty()):
           print ("Queue Empty")
        else:
           data=self.__element[self.__front] 
           self.__front+=1   
        return data
        
    def display(self):
        if (self.is_empty()):
            print("The queue is empty")
        else:
            for index in range(self.__front,self.__rear+1):
                print(self.__elements[index])
            
    def get_max_size(self):
        return self.__max_size