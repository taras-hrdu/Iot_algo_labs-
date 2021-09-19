import random
import time
from enum import Enum
class SortOrder(Enum):
    ASC = 0
    DESC = 1

count = 0
swaps = 0

def random_array(arr_lenght, min_num, max_num):
    return (random.sample(range(min_num,max_num),arr_lenght))


def quick_sort(array, start_pos, end_pos,TypeOfSorting):
    if len(array) <= 1:
        return array

    global count, swaps
    new_pivot_pos=start_pos-1
    pivot = array[end_pos]

    for elem_to_compare_pos in range(start_pos,end_pos):
        count += 1
        if TypeOfSorting == SortOrder.ASC:
            if array[elem_to_compare_pos] <= pivot:
                new_pivot_pos+=1
                swaps += 1
                array[new_pivot_pos], array[elem_to_compare_pos] = array[elem_to_compare_pos], array[new_pivot_pos]
        elif TypeOfSorting == SortOrder.DESC:
            if array[elem_to_compare_pos] >= pivot:
                new_pivot_pos+=1
                swaps += 1
                array[new_pivot_pos], array[elem_to_compare_pos] = array[elem_to_compare_pos], array[new_pivot_pos]
    array[new_pivot_pos+1], array[end_pos] = array[end_pos], array[new_pivot_pos+1]
    return new_pivot_pos+1


def partition(array, TypeOfSorting, start_pos=0, end_pos=None):
    if end_pos==None:
        end_pos=len(array)-1
    if start_pos<end_pos:
        pivot_pos=quick_sort(array,start_pos,end_pos,TypeOfSorting)
        partition(array, TypeOfSorting,start_pos,pivot_pos-1)
        partition(array, TypeOfSorting,pivot_pos+1,end_pos)


if __name__ == '__main__':

    arr_lenght = input()
    min_num = input()
    max_num = input()
    TypeOfSorting = input()

    if TypeOfSorting == "asc":
        TypeOfSorting = SortOrder.ASC
    else:
        TypeOfSorting = SortOrder.DESC

    result = random_array(abs(int(arr_lenght)),int(min_num),int(max_num))

    print(f"QuickSort unsorted:\n"
            f"Comparisons: {count}\n"
            f"Swaps: {swaps}\n"
            f"Result: {result}\n")

    start = time.time()        
    partition(result,TypeOfSorting)
    end = time.time()
    execution_time = (end - start) * 1000

    print(f"QuickSort sorted:\n"
            f"Execution time: {execution_time}ms\n"
            f"Comparisons: {count}\n"
            f"Swaps: {swaps}\n"
            f"Result: {result}\n")