# Assessment 3.2: Queue (First-In, First-Out / FIFO) Dynamic Program
# Reference: Assessment 3.1 - Queue Section

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("[]")
        else:
            print(f"Front -> {self.items} <- Rear")

def main():
    queue = Queue()
    word = "ANTEQUINA"

    print("=== INITIAL STATE ===")
    print("Queue Q = []\n")

    print("=== INSERTION (ENQUEUE) PHASE ===")
    for idx, char in enumerate(word):
        queue.enqueue(char)
        print(f"Step {idx + 1}: Enqueue('{char}') -> Current Queue: ", end="")
        queue.display()

    print("\n=== REMOVAL (DEQUEUE) PHASE ===")
    step_num = 10
    while not queue.is_empty():
        removed = queue.dequeue()
        print(f"Step {step_num}: Dequeue() -> Removes '{removed}' -> Current Queue: ", end="")
        queue.display()
        step_num += 1

    print("\nFinal State: Queue Q = [] (Queue is empty)")

if __name__ == "__main__":
    main()