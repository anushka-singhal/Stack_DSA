stack = []
def push():
    element = input("enter the element")
    stack.append(element)
    print(stack)
    
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed element",e)
        print(stack)

while True:
    print("select operations 1 for push and 2 for pop and 3 for quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("enter the correct operation")
    
    
    