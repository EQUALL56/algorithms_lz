import random


def main():
    arr1 = data_generate(100)
    arr2 = arr1.copy()
    _, swaps_1 = bubble_sort(arr1)
    _, swaps_2 = selection_sort(arr2)

    print(f"{swaps_1} swaps -- bubble_sorting \n {swaps_2} swaps -- selection_sorting")


def data_generate(count: int = 100, min_val: int = -(10**3), max_val: int = 10**3):
    arr = []
    arr = random.choices(range(min_val, max_val), k=count)
    return arr


def bubble_sort(arr):
    swap = 0
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] < arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swap += 1
                print(f"{arr}\n")
    print(f"""Sorted list by BUBBLE: {arr}. \n""")

    return arr, swap


def selection_sort(arr):
    swap = 0
    for i in range(0, len(arr)):
        max_ind = i
        j = i + 1
        while j < len(arr):
            if arr[j] > arr[max_ind]:
                max_ind = j
            j += 1

        if max_ind != i:
            arr[i], arr[max_ind] = arr[max_ind], arr[i]
            swap += 1
            print(f"{arr}\n")
    print(f"""Sorted list by SELECTION: {arr}. \n""")
    return arr, swap


if __name__ == "__main__":
    main()
