#include <iostream>

using namespace std;

struct BP {
    int sys;
    int dia;
};

void insertReading(BP arr[], int& size, int index, int sys, int dia) {
    if (index < 0 || index > size) return;
    for (int i = size; i > index; --i) {
        arr[i] = arr[i - 1];
    }
    arr[index].sys = sys;
    arr[index].dia = dia;
    size++;
}

void deleteOutliers(BP arr[], int& size) {
    int i = 0;
    while (i < size) {
        if (arr[i].sys > 180 || arr[i].sys < 90) {
            for (int j = i; j < size - 1; ++j) {
                arr[j] = arr[j + 1];
            }
            size--;
        } else {
            i++;
        }
    }
}

void searchExtremes(BP arr[], int size) {
    if (size == 0) return;
    int maxSys = arr[0].sys;
    int minSys = arr[0].sys;
    
    for (int i = 1; i < size; ++i) {
        if (arr[i].sys > maxSys) maxSys = arr[i].sys;
        if (arr[i].sys < minSys) minSys = arr[i].sys;
    }
    cout << "Highest systolic: " << maxSys << ", Lowest systolic: " << minSys << endl;
}

void computeAverage(BP arr[], int size) {
    if (size == 0) return;
    int sumSys = 0;
    int sumDia = 0;
    for (int i = 0; i < size; ++i) {
        sumSys += arr[i].sys;
        sumDia += arr[i].dia;
    }
    cout << "Average Systolic: " << (double)sumSys / size << ", Average Diastolic: " << (double)sumDia / size << endl;
}

void printReadings(BP arr[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << "(" << arr[i].sys << "/" << arr[i].dia << ") ";
    }
    cout << endl;
}

int main() {
    BP arr[100] = {{120, 80}, {190, 95}, {110, 70}, {85, 60}, {130, 85}};
    int size = 5;
    
    cout << "Initial readings: ";
    printReadings(arr, size);
    
    insertReading(arr, size, 2, 115, 75);
    cout << "After insertion at index 2: ";
    printReadings(arr, size);
    
    searchExtremes(arr, size);
    computeAverage(arr, size);
    
    deleteOutliers(arr, size);
    cout << "After deleting outliers: ";
    printReadings(arr, size);
    
    return 0;
}
