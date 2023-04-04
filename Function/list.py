class ListNode:

    def __init__(self, newItem):
        self.item = newItem
        self.next = None


class LinkedList():

    def __init__(self): 
        dummy = ListNode('dummy') 
        self.head = dummy
        self.tail = dummy
        self.count = 0 

    def insert(self, i:int, newItem):
        curr = self.head.next

        if i == 0:
            new_node = ListNode(newItem)
            new_node.next = curr
            self.head.next = new_node
            self.count += 1
            return

        for i in range(i-1):
            curr = curr.next
        
        new_node = ListNode(newItem)
        new_node.next = curr
        curr.next = new_node
        self.count += 1

    def append(self, newItem):
        if self.head.next == None:
            new_node = ListNode(newItem)
            self.head.next = new_node
            self.tail = new_node
            self.count += 1
            return       
                    
        new_node = ListNode(newItem)
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1


    def pop(self, i:int):   # i번 노드 삭제. 고정 파라미터
        curr = self.head.next

        if i == 0:
            self.head.next = curr.next
            self.count -= 1
            return

        if i > self.count:
            print('!pop() --> index error')
            return

        for i in range(i-2):
            curr = curr.next

        curr.next = curr.next.next
        self.count -= 1

    def pop_stack(self):
        curr = self.head.next
        
        for i in range(self.count-2):
            curr = curr.next         
        
        self.tail = curr
        curr.next = None
        self.count -= 1
        

    def remove(self, x):
        pass

    def get(self, i:int):
        curr = self.head.next     

        for x in range(self.count):
            if curr.item == i:
                return str(curr.item)               
            curr = curr.next
        return str(i) + ' is Not on the list'


        

    def index(self, x) -> int:
        pass

    def isEmpty(self) -> bool:
        if self.head.next == None:
            return True
        return False

    def size(self) -> int:
        return self.count

    def clear(self):
        self.head.next = None
        self.count = 0

    def list_count(self, x):
        curr = self.head.next
        cnt = 0

        for i in range(self.count):
            if curr.item == x:
                cnt += 1                
            curr = curr.next
        return cnt

    def extend(self, a): # 여기서 a는 self와 같은 타입의 리스트
        self.tail.next = a.head.next
        self.tail = a.tail
        self.count += a.count

    def copy(self):
        pass

    def reverse(self):
        curr = self.head.next
        temp = []

        for i in range(self.count):    
            temp.append(curr.item)
            curr = curr.next

        ct = self.count
        self.clear()

        for i in range(ct-1, -1, -1):
            self.append(temp[i])    


    def merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list     

        mid = len(unsorted_list)//2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]    

        left_ = self.merge_sort(left)
        right_ = self.merge_sort(right)
        return self.merge(left_, right_)

    def merge(self, left, right):
        i, j = 0,0
        sorted_list = []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
        while j < len(right):
            sorted_list.append(right[j])
            j += 1
            
        return sorted_list          

    def sort(self):
        curr = self.head.next
        temp = []

        for i in range(self.count):    
            temp.append(curr.item)
            curr = curr.next       
        
        
        unsorted_list = temp
        sorted_list = self.merge_sort(unsorted_list)

        ct = self.count
        self.clear()

        for i in range(ct):
            self.append(sorted_list[i])  


 

#  (ListNode, ListNode)
    def __findNode(self, x):
        pass

    def __getNode(self, i:int):       
        pass

    def printList(self):
        curr = self.head.next #dummy 제외
        while curr:
            print(curr.item)
            curr = curr.next
        print('count : ', self.count)
        print('-----')
   
   
      
if __name__ == "__main__":

    list = LinkedList()
    list.append(30)
    list.insert(0, 20)
    a = LinkedList()
    a.append(4)
    a.append(3)
    a.append(3)
    a.append(2)
    a.append(1)
    list.extend(a)
    list.reverse()
    list.pop(0)
    list.sort()
    print('count(3):', list.list_count(3))
    print("get(2):", list.get(2))
    list.printList()