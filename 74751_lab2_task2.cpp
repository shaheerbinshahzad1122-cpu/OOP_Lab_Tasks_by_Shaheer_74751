// 74751_lab2_task2.cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<double> spo2_values(8);
    for (int i = 0; i < 8; ++i) {
        cout << "Enter SpO2 reading " << (i + 1) << ": ";
        cin >> spo2_values[i];
    }
    
    int below_90_count = 0;
    int drop_count = 0;
    
    if (spo2_values[0] < 90) {
        below_90_count++;
    }
    
    for (int i = 1; i < 8; ++i) {
        if (spo2_values[i] < 90) {
            below_90_count++;
        }
        if (spo2_values[i] < spo2_values[i-1]) {
            drop_count++;
        }
    }
    
    cout << "Total times SpO2 drops below 90: " << below_90_count << endl;
    cout << "Times a drop occurs compared to previous reading: " << drop_count << endl;
    
    return 0;
}
