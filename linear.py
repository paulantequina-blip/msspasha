def linear_search(data_list, target):
    """
    Step 1: Set i = 0
    Step 2: While i < N:
                If List[i] == Target then: Return i
                Set i = i + 1
    Step 3: Return -1
    """
    i = 0
    n = len(data_list)

    print(f"Searching for target '{target}' in List: {data_list}\n")

    while i < n:
        print(f"Step (i={i}): Compare List[{i}] ('{data_list[i]}') with '{target}'")
        if data_list[i] == target:
            print(f" -> Match found at index {i}!")
            return i
        i += 1

    print(" -> Target not present in List.")
    return -1


def main():
    antequina_list = ['A', 'N', 'T', 'E', 'Q', 'U', 'I', 'N', 'A']
    target_element = 'Q'  # As defined in your execution example

    result = linear_search(antequina_list, target_element)
    print(f"\nResult Index: {result}")


if __name__ == "__main__":
    main()