def main():
    # Step 1: Initialize an empty array arr of size 9
    arr = []
    word = "ANTEQUINA"

    print("=== INITIAL STATE ===")
    print(f"arr = {arr}\n")

    # Step 2: Insert each character of ANTEQUINA sequentially into indices 0 through 8
    print("=== INSERTION PHASE ===")
    for idx, char in enumerate(word):
        arr.append(char)
        print(f"Step {idx + 1}: arr[{idx}] = '{char}' -> Current State: {arr}")

    print(f"\nCurrent Array State: {arr}\n")

    # Step 3: Delete elements starting from index 8 down to 0 until empty
    print("=== REMOVAL PHASE ===")
    step_num = 10
    while len(arr) > 0:
        idx_to_remove = len(arr) - 1
        removed_char = arr.pop()
        print(f"Step {step_num}: Delete index {idx_to_remove} ('{removed_char}') -> Current State: {arr}")
        step_num += 1

    print(f"\nFinal State: {arr} (Array is empty)")


if __name__ == "__main__":
    main()