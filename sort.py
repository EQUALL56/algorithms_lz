import random


def main():
    arr1 = data_generate()
    arr2 = arr1
    bubble_sort(arr1)
    selection_sort(arr2)


def data_generate(count: int = 100, min_val: int = -(10**2), max_val: int = 10**2):
    arr = []
    arr = random.choices(range(min_val, max_val), k=count)
    return arr


def bubble_sort(arr):
    iter = 0
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] < arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                iter += 1
                print(f"{arr}\n")
    print(f"""Sorted list: {arr}.
And count of iterations : {iter}""")
    return arr


def selection_sort(arr):
    iter = 0
    for i in range(0, len(arr)):
        min_ind = i
        j = i + 1
        while j < len(arr):
            if arr[j] > arr[min_ind]:
                min_ind = j
            j += 1

        if min_ind != i:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
            iter += 1
            print(f"{arr}\n")
    print(f"""Sorted list: {arr}.
And count of iterations : {iter}""")
    return arr


if __name__ == "__main__":
    main()
