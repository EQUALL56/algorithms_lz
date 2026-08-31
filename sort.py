import random


def main():
    arr1 = data_generate(10)
    arr2 = arr1.copy()
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
    print(f"""Sorted list by BUBBLE: {arr}.
And count of iterations : {iter} \n""")
    return arr


def selection_sort(arr):
    iter = 0
    for i in range(0, len(arr)):
        max_ind = i
        j = i + 1
        while j < len(arr):
            if arr[j] > arr[max_ind]:
                max_ind = j
            j += 1

        if max_ind != i:
            arr[i], arr[max_ind] = arr[max_ind], arr[i]
            iter += 1
            print(f"{arr}\n")
    print(f"""Sorted list by SELECTION: {arr}.
And count of iterations : {iter} \n""")
    return arr


if __name__ == "__main__":
    main()
