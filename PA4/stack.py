# assignment: programming assignment 4
# author: Fiona Leung
# date: 2/28/2023
# file: stack.py
# input: item to push into stack
# output: stack ADT (list), used in tree.py and calculator.py

class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        return self.items.pop()

     def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

     def size(self):
        return len(self.items)
     

# a driver program for class Stack
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
    
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
    print ("all passed!")