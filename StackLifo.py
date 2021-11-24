class StackLifo():

    def __init__(self):
        self.mystack=[]


    def push(self,element):
        self.mystack.append(element)

    def pop(self):
        if len((self.mystack))>0:
            return self.mystack.pop()
        return None


'''stack= StackLifo()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.pop())'''