# Assessment 3.2: Stack (Last-In, First-Out / LIFO) Dynamic Program
# Reference: Assessment 3.1 - Stack Section

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("[]")
        else:
            print(f"Top -> {list(reversed(self.items))}")

def main():
    stack = Stack()
    word = "ANTEQUINA"

    print("=== INITIAL STATE ===")
    print("Stack S = []\n")

    print("=== INSERTION (PUSH) PHASE ===")
    for idx, char in enumerate(word):
        stack.push(char)
        print(f"Step {idx + 1}: Push('{char}') -> Current Stack: ", end="")
        stack.display()

    print("\n=== REMOVAL (POP) PHASE ===")
    step_num = 10
    while not stack.is_empty():
        removed = stack.pop()
        print(f"Step {step_num}: Pop() -> Removes '{removed}' -> Current Stack: ", end="")
        stack.display()
        step_num += 1

    print("\nFinal State: Stack S = [] (Stack is empty)")

if __name__ == "__main__":
    main()