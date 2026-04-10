class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)

    def push(self, value):
        self.s.insert(0, value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]

    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop(0)
        
stk = stack()
# print(stk.pop()) raise exception
stk.push(10)
stk.push(50)
stk.push(100)

print(stk.peek())

print(stk.pop())
print(stk.pop())
print(stk.pop())