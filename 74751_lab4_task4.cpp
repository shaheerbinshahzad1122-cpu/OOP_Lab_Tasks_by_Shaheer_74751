#include <iostream>

using namespace std;

double calculate_avg_temperature(const double* voltage_readings, int size) {
    if (size == 0) return 0;
    double sum_temp = 0;
    for (int i = 0; i < size; ++i) {
        sum_temp += voltage_readings[i] * 10.0; // Conversion formula
    }
    return sum_temp / size;
}

int filter_noisy_readings(double* readings, int& size, double valid_min, double valid_max) {
    int valid_count = 0;
    for (int i = 0; i < size; ++i) {
        if (readings[i] >= valid_min && readings[i] <= valid_max) {
            readings[valid_count] = readings[i];
            valid_count++;
        }
    }
    size = valid_count; // update effective size
    return valid_count;
}

int main() {
    double voltages[] = {3.5, 3.6, 1.2, 3.8, 9.9, 3.7};
    int size = sizeof(voltages) / sizeof(voltages[0]);
    
    double avg_temp = calculate_avg_temperature(voltages, size);
    cout << "Average Temperature: " << avg_temp << endl;
    
    int valid_cnt = filter_noisy_readings(voltages, size, 3.0, 4.0);
    cout << "Valid count: " << valid_cnt << ", Filtered readings: ";
    for (int i = 0; i < size; ++i) cout << voltages[i] << " ";
    cout << endl;
    
    return 0;
}
