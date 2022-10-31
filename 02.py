from typing import List
def merge_sort(array):
    size=len(data)
    for index in range(size):
        small_index = index
        for jindex in range(index+1, size):
            if array[jindex] < array[small_index]:
                small_index = jindex
        array[small_index],array[index] = array[index], array[small_index]
    print(array)
    

input_data = input()
data = []
for item in input_data.split(', '):
    if item.isnumeric():
        data.append(int(item))
    elif item.lstrip("-").isnumeric():
        data.append(int(item))
merge_sort(data)
