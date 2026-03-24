queue = []

def insert():
    item = int(input("Enter element to insert: "))
    queue.append(item)
    print(item, "inserted into queue")

def delete():
    if len(queue) == 0:
        print("Queue is empty, cannot delete")
    else:
        removed_item = queue.pop(0)
        print(removed_item, "deleted from queue")

def traversal():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements are:")
        for element in queue:
            print(element)

while True:
    print("\nQueue Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        traversal()
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice, please try again")