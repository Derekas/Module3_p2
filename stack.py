stack = []


def pop():
    if len(stack)>0:

        val=stack.pop()
        return val
    else:
        return None


def push(val):
    stack.append(val)


push(10)
push(20)
push(30)

print(pop())
print(pop())
print(pop())