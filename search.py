import random


def main():
    arr = data_gen()
    print(f"{arr} \n")
    i = random.choice(range(0, 100))
    element = arr[i]

    ind1, compare1 = bin_search(arr, element)
    print(
        f"Binary : Element {element} have serched by {compare1} compares with index = {ind1}"
    )

    ind2 = line_search(arr, element)

    if ind2 is not None:
        print(
            f"Line : Element {element} have serched by {ind2 + 1} compares with index = {ind2}"
        )

    # ind3 = rec_bin_search(arr, element)
    # print(f"Rec : Element {element} have serched by with index = {ind3}")


def line_search(arr, aim):
    if len(arr) == 0:
        return None

    for i in range(0, len(arr)):
        if arr[i] == aim:
            return i
    print("Element does not exist")
    return None


def bin_search(arr: list, aim: int):
    left, right = 0, len(arr) - 1
    compare = 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == aim:
            return mid, compare
        elif arr[mid] < aim:
            left = mid + 1
            compare += 1
        else:
            right = mid - 1
            compare += 1

    print("Element does not exist")
    return None, 0


def data_gen(count=100, start=0, stop=1000):
    arr = []
    arr = random.sample(range(start, stop), count)
    return sorted(arr)


def rec_bin_search(arr: list, aim: int, left: int = 0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == aim:
        return mid
    elif arr[mid] < aim:
        return rec_bin_search(arr, aim, mid + 1, right)
    else:
        return rec_bin_search(arr, aim, left, mid - 1)


if __name__ == "__main__":
    main()
