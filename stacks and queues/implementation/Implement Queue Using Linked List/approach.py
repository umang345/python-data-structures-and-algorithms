class Node:
    def __init__(self, value):
        self.data = value  # storing the incoming value passed by user in the data property
        self.next = None
class Queue:
    def __init__(self):
        # Create an instance of the LinkedList
        self.linkedList = LinkedList()

    def enqueue(self, data):
        self.linkedList.add_at_tail(data)

    def is_empty(self):
        return self.linkedList.is_empty()

    def dequeue(self):
        if self.linkedList.is_empty():
            return -1
        return self.linkedList.remove_from_head()



class LinkedList:
    def __init__(self):
        self.head = None  # points to the first element of the list
        self.tail = None  # points to the last element of the list

    def add_at_tail(self, data):
        new_node = Node(data)  # create a new node

        if self.head is None:
            # If the list is empty, both head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, add the new node to the tail
            self.tail.next = new_node  # Connect the current tail to the new node
            self.tail = new_node  # Update tail to point to the new node

    def remove_from_head(self):
        if self.head is None:
            return None  # If the list is empty, nothing to remove
        if self.head.next is None:
            # If the list has only one element, set both head and tail to None
            data = self.head.data
            self.head = None
            self.tail = None
            return data

        # If the list has more than one element, remove the head and return its data
        data = self.head.data
        self.head = self.head.next
        return data

    def is_empty(self):
        return self.head is None  # Returns True if the list is empty, else False

    def get_head(self):
        if self.is_empty():
            return None
        return self.head.data  # Return the data of the head node





# Input and processing
q = int(input())  # Read the number of queries
queries = []

# Read each query from the user
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Create an instance of the Queue
queue = Queue()

output = []

# Process each query
for query in queries:
    if query[0] == 1:  # Enqueue operation
        queue.enqueue(query[1])
    elif query[0] == 2:  # Dequeue operation
        result = queue.dequeue()
        output.append(str(result))  # Store the result of dequeue in the output list

# Print the results of all type 2 queries (dequeues) in one line, space-separated
print(" ".join(output))
