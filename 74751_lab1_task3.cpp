// 74751_lab1_task3.cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double alpha, beta;
    cout << "Enter alpha band amplitude: ";
    cin >> alpha;
    cout << "Enter beta band amplitude: ";
    cin >> beta;
    
    double r = (beta * beta) / (alpha * alpha);
    double cli = log10(r * 100);
    
    cout << "Power Ratio (R): " << r << endl;
    cout << "Cognitive Load Index (CLI): " << cli << endl;
    
    return 0;
}
