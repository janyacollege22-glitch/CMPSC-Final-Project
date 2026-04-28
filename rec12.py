# Recitation Activity #12
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.current_node = -1

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        return self.count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.count+=1

   
    def __getitem__(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return current
            else:
                current=current.next
        return None
    
    def __next__(self):
        if self.current_node is None or self.isEmpty():
            raise StopIteration
        else: 
            if self.current_node == -1:
                self.current_node=self.head

            current = self.current_node
            self.current_node = self.current_node.next
            return current

def traverse(linked_object):
        current=linked_object.head
        while current:
            yield current
            current=current.next

def hailstone(num):
    '''
        >>> my_gen = hailstone(6) 
        >>> [item for item in my_gen]
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
        >>> my_gen = hailstone(5) 
        >>> next(my_gen) 
        5
        >>> next(my_gen)
        16
        >>> next(my_gen)
        8
        >>> next(my_gen)
        4
        >>> next(my_gen)
        2
        >>> next(my_gen)
        1
        >>> next(my_gen)
        Traceback (most recent call last):
        StopIteration
    '''
    # Your code here
    if num <= 0:
        raise ValueError("Input must be a positive integer.")
    if num == 1:
        yield 1
    else:
        yield num
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            yield num
    


    pass