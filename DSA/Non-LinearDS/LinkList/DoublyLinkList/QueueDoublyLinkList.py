
# class Node:
#     def __init__(self, d):
#         self.data = d
#         self.previous = None
#         self.next = None

# class DoublyLinkedQueue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueue(self):
#         data = int(input('Enter the element you want to add to the queue: '))
#         new_node = Node(data)
#         if self.rear is None:  # Queue is empty
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             new_node.previous = self.rear
#             self.rear = new_node

#     def dequeue(self):
#         if self.front is None:  # Queue is empty
#             print("Queue is empty, cannot dequeue.")
#             return
#         removed_data = self.front.data
#         self.front = self.front.next
#         if self.front is None:  # Queue is now empty
#             self.rear = None
#         else:
#             self.front.previous = None
#         print(f"Dequeued: {removed_data}")

#     def display_forward(self):
#         current = self.front
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def display_backward(self):
#         current = self.rear
#         while current is not None:
#             print(current.data, end=" -> ")
#             current = current.previous
#         print("None")

# # Driver code
# if __name__ == "__main__":
#     queue = DoublyLinkedQueue()
#     while True:
#         print('    DOUBLY LINKED QUEUE OPERATION      ')
#         print('         1. ENQUEUE      ')
#         print('         2. DEQUEUE       ')
#         print('         3. Display Forward       ')
#         print('         4. Display Backward       ')
#         print('         5. EXIT       ')

#         choice = int(input('Enter your choice: '))

#         if choice == 1:
#             queue.enqueue()
#         elif choice == 2:
#             queue.dequeue()
#         elif choice == 3:
#             queue.display_forward()
#         elif choice == 4:
#             queue.display_backward()
#         elif choice == 5:
#             break
#         else:
#             print('Wrong Choice')
