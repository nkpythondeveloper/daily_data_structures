# Array Implementation
"""
Python's inbuilt LIST data structure is an array.

ARRAY - Minimal Implementation

Now, what are the important operations that can be done with Arrays?

1. INSERT
2. GET[INDEX]
3. UPDATE[INDEX,VALUE]
4. DELETE[INDEX]

"""

class CustomArray:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def get(self, index):
        return self.data[index]
    
    def update(self, index, value):
        self.data[index] = value

    def delete(self, index):
        return self.data.pop(index)
    

if __name__ == "__main__":

    # Instantiated the custom array object
    a = CustomArray()

    # Insert item
    a.insert(10)
    a.insert(20)
    print(a.data)

    # Update item at a index
    a.update(1, 30)
    print(a.data)

    # Delete item at a index
    a.delete(0)
    print(a.data)