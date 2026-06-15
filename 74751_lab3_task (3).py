def insert_reading(arr, index, sys, dia):
    arr.append([0, 0])
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = [sys, dia]

def delete_outliers(arr):
    i = 0
    while i < len(arr):
        if arr[i][0] > 180 or arr[i][0] < 90:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()
        else:
            i += 1

def search_extremes(arr):
    if not arr: return
    max_sys = arr[0][0]
    min_sys = arr[0][0]
    
    for i in range(1, len(arr)):
        if arr[i][0] > max_sys: max_sys = arr[i][0]
        if arr[i][0] < min_sys: min_sys = arr[i][0]
    print(f"Highest systolic: {max_sys}, Lowest systolic: {min_sys}")

def compute_average(arr):
    if not arr: return
    sum_sys = 0
    sum_dia = 0
    count = 0
    for reading in arr:
        sum_sys += reading[0]
        sum_dia += reading[1]
        count += 1
    print(f"Average Systolic: {sum_sys / count}, Average Diastolic: {sum_dia / count}")

if __name__ == "__main__":
    arr = [[120, 80], [190, 95], [110, 70], [85, 60], [130, 85]]
    
    print(f"Initial readings: {arr}")
    
    insert_reading(arr, 2, 115, 75)
    print(f"After insertion at index 2: {arr}")
    
    search_extremes(arr)
    compute_average(arr)
    
    delete_outliers(arr)
    print(f"After deleting outliers: {arr}")
