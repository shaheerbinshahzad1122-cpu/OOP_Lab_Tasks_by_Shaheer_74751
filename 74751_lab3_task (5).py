def insert_sample(arr, index, value):
    arr.append(0)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value

def remove_noise(arr, min_range, max_range):
    i = 0
    while i < len(arr):
        if arr[i] < min_range or arr[i] > max_range:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()
        else:
            i += 1

def find_peaks(arr):
    if not arr: return
    max_peak = arr[0]
    min_peak = arr[0]
    for val in arr:
        if val > max_peak: max_peak = val
        if val < min_peak: min_peak = val
    print(f"Max Peak: {max_peak}, Min Peak: {min_peak}")

def reverse_signal(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

def count_crossings(arr, threshold):
    count = 0
    for i in range(len(arr) - 1):
        if (arr[i] < threshold and arr[i + 1] >= threshold) or \
           (arr[i] >= threshold and arr[i + 1] < threshold):
            count += 1
    return count

if __name__ == "__main__":
    arr = [90, 110, 250, 80, -10, 105, 95]
    print(f"Initial ECG: {arr}")
    
    insert_sample(arr, 3, 100)
    print(f"After insertion at index 3: {arr}")
    
    remove_noise(arr, 0, 200)
    print(f"After removing noise: {arr}")
    
    find_peaks(arr)
    
    print(f"Threshold crossings (100): {count_crossings(arr, 100)}")
    
    reverse_signal(arr)
    print(f"Reversed ECG: {arr}")
