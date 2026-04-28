class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class Malloc_Library:
    
    def __init__(self):
        self.head=None
        self.tail=None

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
        current=self.head
        count=0
        while current is not None:
            count += 1
            current = current.next    
        return count
    
    def __setitem__(self, key, value):
        if key < 0 or key >= len(self):
            raise IndexError("Index out of range")
        else:             
            current = self.head
            for i in range(key):
                current = current.next
            current.value = value
        pass

    def __getitem__(self, key):
        if key < 0 or key >= len(self):
            raise IndexError("Index out of range")
        else:             
            current = self.head
            for i in range(key):
                current = current.next
            return current.value
        
        pass

    def malloc(self, size):
        newNode=Node(None)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    
    def calloc(self, size):
        newNode=Node(0)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    
    def free(self):
        if self.isEmpty():
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current

    def realloc(self, new_size):
        current_size = len(self)
        if new_size < current_size:
            for _ in range(current_size - new_size):
                self.free()
        elif new_size > current_size:
            for _ in range(new_size - current_size):
                self.malloc(1)
    
    def memcpy(self, dest_index, src_index, size):
        if dest_index < 0 or src_index < 0 or size < 0:
            raise IndexError("Index and size must be non-negative")
        if src_index + size > len(self) or dest_index + size > len(self):
            raise IndexError("Source or destination range is out of bounds")
        
        # Create a temporary list to hold the values to be copied
        temp_values = []
        current = self.head
        for i in range(src_index):
            current = current.next
        for i in range(size):
            temp_values.append(current.value)
            current = current.next
        
        # Copy the values to the destination index
        current = self.head
        for i in range(dest_index):
            current = current.next
        for value in temp_values:
            current.value = value
            current = current.next


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    

    def duplicate(self, item):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return
        current=self.head   
        while current is not None:
            if current.value == item:
                newNode=Node(item)
                newNode.next=current.next
                current.next=newNode
                current=newNode.next
            else:
                current=current.next
        pass
