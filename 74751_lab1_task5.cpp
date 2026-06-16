// 74751_lab1_task5.cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double r, xc, height;
    cout << "Enter body resistance (R): ";
    cin >> r;
    cout << "Enter reactance (Xc): ";
    cin >> xc;
    cout << "Enter height (in cm): ";
    cin >> height;
    
    double z = sqrt(r*r + xc*xc);
    double tbw = (0.6 * height * height) / z;
    
    cout << "Impedance (Z): " << z << endl;
    cout << "Total Body Water (TBW): " << tbw << endl;
    
    return 0;
}
