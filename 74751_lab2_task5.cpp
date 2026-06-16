// 74751_lab2_task5.cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<double> intervals(10);
    for (int i = 0; i < 10; ++i) {
        cout << "Enter breathing interval " << (i + 1) << " (seconds): ";
        cin >> intervals[i];
    }
    
    int total_apnea_events = 0;
    int severe_apnea_count = 0;
    
    for (int i = 0; i < 10; ++i) {
        if (intervals[i] > 10) {
            total_apnea_events++;
        }
    }
    
    for (int i = 1; i < 10; ++i) {
        if (intervals[i] > 10 && intervals[i-1] > 10) {
            severe_apnea_count++;
        }
    }
    
    cout << "Total apnea events: " << total_apnea_events << endl;
    cout << "Severe apnea count: " << severe_apnea_count << endl;
    
    return 0;
}
