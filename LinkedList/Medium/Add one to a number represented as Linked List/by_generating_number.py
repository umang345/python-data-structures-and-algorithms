class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addOne(head: Node) -> Node:
    generatedNum = 0

    temp = head
    while not temp is None:
        generatedNum*=10
        generatedNum+=temp.data
        nodeToDel = temp
        temp = temp.next
        del nodeToDel 

    generatedNum+=1

    head = None 
    if generatedNum == 0:
        return Node(0)
    
    while generatedNum!=0:
        lastDigit = generatedNum%10
        newNode = Node(lastDigit)
        if head is None:
            head = newNode
        else:
            newNode.next = head 
            head = newNode
        generatedNum//=10
    
    return head
