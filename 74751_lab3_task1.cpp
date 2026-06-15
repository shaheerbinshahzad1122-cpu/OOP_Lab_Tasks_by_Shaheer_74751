#include <iostream>

using namespace std;

void insertReading(int arr[], int& size, int index, int value) {
    if (index < 0 || index > size) return;
    for (int i = size; i > index; --i) {
        arr[i] = arr[i - 1];
    }
    arr[index] = value;
    size++;
}

void deleteReading(int arr[], int& size, int value) {
    int i = 0;
    while (i < size) {
        if (arr[i] == value) {
            for (int j = i; j < size - 1; ++j) {
                arr[j] = arr[j + 1];
            }
            size--;
        } else {
            i++;
        }
    }
}

void searchAbnormal(int arr[], int size) {
    cout << "Abnormal heart rates: ";
    for (int i = 0; i < size; ++i) {
        if (arr[i] > 100 || arr[i] < 60) {
            cout << arr[i] << " ";
        }
    }
    cout << endl;
}

void reverseSequence(int arr[], int size) {
    for (int i = 0; i < size / 2; ++i) {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}

int countTachycardia(int arr[], int size) {
    int count = 0;
    for (int i = 0; i < size; ++i) {
        if (arr[i] > 100) {
            count++;
        }
    }
    return count;
}

int main() {
    int arr[100] = {70, 80, 110, 55, 90, 105, 75};
    int size = 7;

    cout << "Initial readings: ";
    for (int i=0; i<size; i++) cout << arr[i] << " ";
    cout << endl;

    insertReading(arr, size, 2, 95);
    cout << "After insertion at index 2: ";
    for (int i=0; i<size; i++) cout << arr[i] << " ";
    cout << endl;

    deleteReading(arr, size, 55);
    cout << "After deleting 55: ";
    for (int i=0; i<size; i++) cout << arr[i] << " ";
    cout << endl;

    searchAbnormal(arr, size);

    reverseSequence(arr, size);
    cout << "After reversal: ";
    for (int i=0; i<size; i++) cout << arr[i] << " ";
    cout << endl;

    cout << "Tachycardia count: " << countTachycardia(arr, size) << endl;

    return 0;
}
