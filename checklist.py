checklist = []

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def listAllItems():
    index = 0
    for item in checklist:
        print('Index:', index, 'Item:', item)
        index += 1

def markCompleted(index):
    checklist[index] = '√' + checklist[index]

def select(code):
    if code == "A":
        item = input("Input item: ")
        create(item)
    elif code == "R":
        index = int(input("Index Number? "))
        read(index)
    elif code == "D":
        listAllItems()
    elif code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test():
    running = True
    while running:
        selection = input("Press A to add to list, R to Read from list, D to display list, and Q to quit: ")
        running = select(selection)

test()
