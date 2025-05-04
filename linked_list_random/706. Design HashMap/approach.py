class ListNode:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ ListNode(-1,-1) for index in range(10**4)]

    def put(self, key: int, value: int) -> None:
        head = self.__get_list_head(key)

        if head.next is None:
            head.next = ListNode(key, value)
            return
        
        if self.get(key) != -1:
            temp = head.next
            while not temp is None:
                if temp.key == key:
                    temp.val = value
                    return
                temp = temp.next
        else:
            temp = head.next
            while not temp.next is None:
                temp = temp.next
            temp.next = ListNode(key, value)



    def get(self, key: int) -> int:
        head = self.__get_list_head(key).next
        
        while not head is None:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1


    def remove(self, key: int) -> None:
        head = self.__get_list_head(key)
        
        if head.next is None:
            return
        if head.next.key == key:
            head.next = head.next.next
            return
        
        temp = head.next
        while not temp.next is None:
            if temp.next.key == key:
                temp.next = temp.next.next
                break
            temp = temp.next


    def __get_list_head(self, key) -> ListNode:
        index = key%(10**4)
        return self.hashmap[index]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)