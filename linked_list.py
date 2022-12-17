class Node:
    def __init__(self , data = None , next = None):
        self.data =data
        self.next =next

class LinkedList:
    def __init__(self):
        self._head = None

    def push(self,data):
        if not self._head:
            self._head = Node(data)
        else:
            self._head = Node(data, self._head)

    def pop(self):
        if not self._head:
            return None

        data =self._head.data
        self._head =self._head.next
        return data


