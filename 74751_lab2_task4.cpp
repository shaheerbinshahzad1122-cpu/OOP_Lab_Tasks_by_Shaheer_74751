// 74751_lab2_task4.cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<double> flow_rates(6);
    for (int i = 0; i < 6; ++i) {
        cout << "Enter flow rate " << (i + 1) << " (ml/hr): ";
        cin >> flow_rates[i];
    }
    
    int risk_counter = 0;
    int critical_event_counter = 0;
    
    for (int i = 0; i < 6; ++i) {
        if (flow_rates[i] > 50) {
            risk_counter++;
        }
    }
    
    for (int i = 1; i < 6; ++i) {
        if (flow_rates[i] > 50 && flow_rates[i-1] > 50) {
            critical_event_counter++;
        }
    }
    
    cout << "Risk counter: " << risk_counter << endl;
    cout << "Critical event counter: " << critical_event_counter << endl;
    
    return 0;
}
