// 74751_lab1_task4.cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double c0, k, t;
    cout << "Enter initial drug concentration (C0): ";
    cin >> c0;
    cout << "Enter elimination rate constant (k): ";
    cin >> k;
    cout << "Enter time (t): ";
    cin >> t;
    
    double c = c0 * exp(-k * t);
    double percentage = (c / c0) * 100;
    
    cout << "Current concentration (C): " << c << endl;
    cout << "Percentage of drug remaining: " << percentage << "%" << endl;
    
    return 0;
}
