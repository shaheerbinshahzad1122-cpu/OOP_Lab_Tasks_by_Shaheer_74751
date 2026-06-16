// 74751_lab1_task2.cpp
#include <iostream>

using namespace std;

int main() {
    double vo2, hr;
    cout << "Enter oxygen consumption (VO2 in ml/kg/min): ";
    cin >> vo2;
    cout << "Enter heart rate (HR): ";
    cin >> hr;
    
    double li = (hr * 0.02) + (vo2 * 0.03);
    double fs = (li * li) / 10;
    
    cout << "Lactate Index (LI): " << li << endl;
    cout << "Fatigue Score (FS): " << fs << endl;
    
    return 0;
}
