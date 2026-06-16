// 74751_lab2_task1.cpp
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    vector<double> rr_intervals(6);
    for (int i = 0; i < 6; ++i) {
        cout << "Enter RR interval " << (i + 1) << " (seconds): ";
        cin >> rr_intervals[i];
    }
    
    int irregularity_count = 0;
    for (int i = 1; i < 6; ++i) {
        if (abs(rr_intervals[i] - rr_intervals[i-1]) > 0.2) {
            irregularity_count++;
        }
    }
    
    cout << "Irregularity count: " << irregularity_count << endl;
    if (irregularity_count > 2) {
        cout << "Potential arrhythmia flagged." << endl;
    }
    
    return 0;
}
