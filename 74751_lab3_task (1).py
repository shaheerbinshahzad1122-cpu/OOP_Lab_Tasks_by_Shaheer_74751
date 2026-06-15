def insert_reading(arr, index, value):
    arr.append(0)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value

def delete_reading(arr, value):
    i = 0
    while i < len(arr):
        if arr[i] == value:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()
        else:
            i += 1

def search_abnormal(arr):
    abnormal = []
    for val in arr:
        if val > 100 or val < 60:
            abnormal.append(val)
    return abnormal

def reverse_sequence(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

def count_tachycardia(arr):
    count = 0
    for val in arr:
        if val > 100:
            count += 1
    return count

if __name__ == "__main__":
    arr = [70, 80, 110, 55, 90, 105, 75]
    print(f"Initial readings: {arr}")
    
    insert_reading(arr, 2, 95)
    print(f"After insertion at index 2: {arr}")
    
    delete_reading(arr, 55)
    print(f"After deleting 55: {arr}")
    
    print(f"Abnormal heart rates: {search_abnormal(arr)}")
    
    reverse_sequence(arr)
    print(f"After reversal: {arr}")
    
    print(f"Tachycardia count: {count_tachycardia(arr)}")
