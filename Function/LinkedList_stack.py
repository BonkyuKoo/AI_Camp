import list

class LinkedStack:
    def __init__(self):
        self.__list = list.LinkedList()
    
    def push(self, x):
        self.__list.append(x)        
        pass
    
    def pop(self):
        self.__list.pop_stack()
        pass
    
    def top(self):
        return self.__list.tail.item
    
    def isEmpty(self):
        if self.__list.count == 0:
            return True

        return False
    
    def popAll(self):
        self.__list.clear()
        self.__list.tail == self.__list.head
        self.__list.count = 0
    
    def printAll(self):
        self.__list.printList()        
    

s1 = LinkedStack()
s1.push(100)
s1.push(200)
print('Top is', s1.top())
s1.pop()
s1.push('Monday')
s1.printAll()
print('isEmpty?', s1.isEmpty())

