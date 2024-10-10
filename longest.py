def find_longest(arr):
    longest = arr[0]
    for i in range(1, len(arr)):
        if len(arr[i]) > len(longest):
            longest = arr[i]
    return longest


if __name__ == "__main__":
    print(find_longest(["yellow", "red", "blue", "green"]))
