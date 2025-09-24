# Stack Implementation
"""
Python's inbuilt LIST data structure is more over a stack.

STACK - 

Is a data structure where the FIFO (First In - First Out),
methodology is followed.

Whatever was stacked last, will be fetched first.

Think of a PAN CAKE analogy.

Now, what are the important operations that can be done with Stacks?

1. PUSH
2. POP
3. PEEK

Push - 
Similar to append to list, adds item to the last index

Time Complexity = O(1)

Pop - 
Similar to pop from list, gets the item from the last index

Time Complexity = O(1)

Peek -
Similar to accessing the element at last index in list, list[-1]

Time Complexity = O(1)

"""
# Simple, classic list using Class implementation of Stack.

class Stack:
    def __init__(self, items=None):
        self.data = []
        if items:
            self.data.extend(items)
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.data:
            raise IndexError("Pop from empty list, not possible!")
        return self.data.pop()
    
    def peek(self):
        if not self.data:
            raise IndexError("Peeking into a empty list, not possible!")
        return self.data[-1]
    
    def is_empty(self):
        return not self.data
    
    def __len__(self):
        return len(self.data)
    

if __name__ == "__main__":
    # Instantiated a Stack Object
    s = Stack()
    # push item
    s.push(10)
    s.push(20)
    # take a peek, whats at the top
    print(s.peek())
    # pop the item
    s.pop()
    # again take a peek, what at the new top
    print(s.peek())
    # pop that too
    s.pop()
    # now if we take a peek, should raise an index error
    print(s.peek())