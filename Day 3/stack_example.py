class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__top = -1
        
    def is_full(self):
        if self.__top == self.__max_size-1:
            return True
        else:
            return False
        
    def is_empty(self):
        if self.__top == -1:
            return True
        else:
            return False
        
    def push(self,data):
        if self.is_full():
            print("Stack overflow!!!!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data
            
    def pop(self):
        if self.is_empty():
            print("Stack underflow!!!")
        else:
            data = self.__elements[self.__top]
            top = top -1
            return data
   
    def display(self):
        if self.is_empty():
            print("Stack is empty!!")
        else:
            i = self.__top

stack1 = Stack(5)
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)
stack1.display()
