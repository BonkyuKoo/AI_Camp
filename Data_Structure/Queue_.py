#Queue

class Queue:      
    def __init__(self):
        self.__queue = []
        self.count = 0


    def enqueue(self, data):  
        self.__queue.append(data)
        self.count += 1


    def dequeue(self):
        self.__queue.pop(0)
        self.count -= 1


    def front(self):
        return self.__queue[0]     


    def isEmpty(self):
        if self.count == 0:
            return True
        
        return False


    def dequeueAll(self):
        self.__queue.clear()
        self.count = 0


    def printQueue(self):
        print('--print--')
        for i in range(self.count):
            print(self.__queue[i])


if __name__ == '__main__':
    q1 = Queue()
    q1.enqueue("Mon")
    q1.enqueue("Tue")
    q1.enqueue(1234)
    q1.enqueue("Wed")
    q1.dequeue()
    q1.enqueue('aaa')
    q1.printQueue()