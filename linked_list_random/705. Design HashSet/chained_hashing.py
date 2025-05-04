class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(-1) for index in range(10**4)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            index = self.__get_index(key)
            head = self.set[index].next    
            
            if head is None:
                self.set[index].next = ListNode(key)
            else:
                while not head.next is None:
                    head = head.next
                head.next = ListNode(key)


    def remove(self, key: int) -> None:
        index = self.__get_index(key)
        head = self.set[index].next

        if head is None:
            return
        if head.val == key:
            self.set[index].next = self.set[index].next.next
            return

        trav = head
        while not trav is None and not trav.next is None:
            if trav.next.val == key:
                trav.next = trav.next.next
                break
            else:
                trav = trav.next 


    def contains(self, key: int) -> bool:
        index = self.__get_index(key)
        head = self.set[index].next

        while not head is None:
            if head.val == key:
                return True
            head = head.next
        return False

    def __get_index(self, key) -> int:
        return key % (10**4)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)