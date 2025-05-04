class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addOne(head: Node) -> Node:
    head,carry = helper(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head 
        head = newNode

    return head

def helper(head:Node) -> tuple[Node,int]:
    if head is None:
        head = Node(1)
        return (head,0)
    
    if head.next is None:
        currSum = head.data+1
        carry = 0
        if currSum>9:
            carry=1
            currSum=currSum%10
            head.data = currSum
        head.data = currSum
        return (head,carry)

    head.next, carry = helper(head.next)
    if carry == 1:
        currSum = head.data+1
        if currSum>9:
            carry=1
            currSum=currSum%10
        else:
            carry=0
        head.data = currSum
    
    return (head, carry)