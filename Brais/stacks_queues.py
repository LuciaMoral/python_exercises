# stacks - LIFO (last in/first out)
stack = []
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)
stack_item = stack[len(stack)-1]
del stack[len(stack)-1]
stack.pop()
print(stack_item)
print(stack)

# queue - FIFO (first in/first out)

queue = []
queue.append("tomatoes")
queue.append(2)
queue.append(4)

print(queue)

#dequeue

queue.pop(0)
print(queue)

# extra web

def web_navigation():
    stack = []
    while True:
        action = input("add a url or navigate with words next/back/exit: ")

        if action == "exit":
            print("exiting nav web")
            break
        elif action == "next":
            pass # we cannot implement stack here
        elif action == "back":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)


        if len(stack) > 0:
            print(f"you have navigated to web: {stack[len(stack) - 1]}")
        else:
             print("you are on the first web")

# web_navigation()


def shared_printer():
    queue = []
    while True:
        action = input("add document or  print/exit: ")
        if action == "exit":
            print("exiting printer...")
            break
        elif action == "print":
             if len(queue) > 0:
                print(f"printing: {queue.pop(0)}")
        else:
            queue.append(action)
        if len(queue) > 0:
            print(f"printer queue is: {queue}")
        else:
            print("there are no more docs")
shared_printer()
