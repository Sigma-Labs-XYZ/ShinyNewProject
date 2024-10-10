def find_longest(arr: list) -> str:
    longest = arr[1]
    for i in range(1, len(arr)):
        if len(arr[i]) > len(longest):
            longest = arr[i]
        return longest


if __name__ == "__main__":
    print(find_longest(["yellow", "red", "blue", "green"]))
