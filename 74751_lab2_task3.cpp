// 74751_lab2_task3.cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<double> amplitudes(7);
    for (int i = 0; i < 7; ++i) {
        cout << "Enter amplitude reading " << (i + 1) << ": ";
        cin >> amplitudes[i];
    }
    
    int total_decreases = 0;
    int current_consecutive_decreases = 0;
    int max_consecutive_decreases = 0;
    
    for (int i = 1; i < 7; ++i) {
        if (amplitudes[i] < amplitudes[i-1]) {
            total_decreases++;
            current_consecutive_decreases++;
            if (current_consecutive_decreases > max_consecutive_decreases) {
                max_consecutive_decreases = current_consecutive_decreases;
            }
        } else {
            current_consecutive_decreases = 0;
        }
    }
    
    cout << "Total decrease count: " << total_decreases << endl;
    cout << "Max consecutive decrease count: " << max_consecutive_decreases << endl;
    
    return 0;
}
