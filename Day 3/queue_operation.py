class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index],end=" ")
        print()
                                       
num_queue=Queue(7)
num_queue.enqueue(2)
num_queue.enqueue(7)
num_queue.enqueue(9)
num_queue.enqueue(4)
num_queue.enqueue(6)
num_queue.enqueue(5)
num_queue.enqueue(10)