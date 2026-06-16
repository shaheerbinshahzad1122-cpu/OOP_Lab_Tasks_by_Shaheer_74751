// 74751_lab1_task1.cpp
#include <iostream>

using namespace std;

int main() {
    double distance, time;
    cout << "Enter distance between ECG and PPG sensors (meters): ";
    cin >> distance;
    cout << "Enter time delay (seconds): ";
    cin >> time;
    
    double pwv = distance / time;
    double sbp = 120 + (pwv - 5) * 10;
    
    cout << "Pulse Wave Velocity (PWV): " << pwv << endl;
    cout << "Systolic Blood Pressure (SBP): " << sbp << endl;
    
    return 0;
}
