#include <iostream>

using namespace std;

void find_peaks(const double* ecg_values, int size, double* max_peak, double* min_peak) {
    if (size == 0) return;
    *max_peak = ecg_values[0];
    *min_peak = ecg_values[0];
    for (int i = 1; i < size; ++i) {
        if (ecg_values[i] > *max_peak) *max_peak = ecg_values[i];
        if (ecg_values[i] < *min_peak) *min_peak = ecg_values[i];
    }
}

int apply_baseline_correction(double* ecg_values, int size) {
    if (size == 0) return 0;
    double sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += ecg_values[i];
    }
    double avg = sum / size;
    for (int i = 0; i < size; ++i) {
        ecg_values[i] -= avg;
    }
    return size;
}

int main() {
    double ecg[] = {1.2, 0.5, 2.3, -0.4, 1.1};
    int size = sizeof(ecg) / sizeof(ecg[0]);
    
    double max_peak, min_peak;
    find_peaks(ecg, size, &max_peak, &min_peak);
    cout << "Max Peak: " << max_peak << ", Min Peak: " << min_peak << endl;
    
    int corrected = apply_baseline_correction(ecg, size);
    cout << "Corrected samples: " << corrected << ", New values: ";
    for (int i = 0; i < size; ++i) cout << ecg[i] << " ";
    cout << endl;
    
    return 0;
}
