# Assessment 3.2: Singly Linked List Dynamic Program
# Reference: Assessment 3.1 - Singly Linked List Section

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    def display(self):
        if not self.head:
            print("NULL")
            return
        current = self.head
        elements = []
        while current:
            elements.append(f"[{current.data}]")
            current = current.next
        print(" -> ".join(elements) + " -> NULL")

def main():
    llist = SinglyLinkedList()
    word = "ANTEQUINA"

    print("=== INITIAL STATE ===")
    print("head = NULL, tail = NULL\n")

    print("=== INSERTION (APPEND) PHASE ===")
    for idx, char in enumerate(word):
        llist.append(char)
        print(f"Step {idx + 1}: Append node [{char}] -> ", end="")
        llist.display()

    print("\n=== REMOVAL (DELETE HEAD) PHASE ===")
    step_num = 10
    while llist.head:
        removed = llist.delete_head()
        print(f"Step {step_num}: Delete head [{removed}] -> ", end="")
        llist.display()
        step_num += 1

    print("\nFinal State: head = NULL (Linked List is empty)")

if __name__ == "__main__":
    main()