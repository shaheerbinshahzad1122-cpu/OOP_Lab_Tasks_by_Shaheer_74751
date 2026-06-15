#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

void calculate_stats(const vector<double>* hemoglobin_levels, double& average, double& std_dev) {
    if (hemoglobin_levels->empty()) {
        average = 0;
        std_dev = 0;
        return;
    }
    double sum = 0;
    for (double val : *hemoglobin_levels) {
        sum += val;
    }
    average = sum / hemoglobin_levels->size();
    
    double var_sum = 0;
    for (double val : *hemoglobin_levels) {
        var_sum += (val - average) * (val - average);
    }
    std_dev = sqrt(var_sum / hemoglobin_levels->size());
}

bool insert_test_result(vector<double>* results, double new_result, int index) {
    if (index >= 0 && index <= results->size()) {
        results->insert(results->begin() + index, new_result);
        return true;
    }
    return false;
}

string assess_risk(string patient_id, double cholesterol, double blood_pressure, double fasting_sugar) {
    int risk = 0;
    if (cholesterol > 200) risk++;
    if (blood_pressure > 130) risk++;
    if (fasting_sugar > 100) risk++;
    
    if (risk >= 2) return "Patient " + patient_id + ": High Risk";
    if (risk == 1) return "Patient " + patient_id + ": Moderate Risk";
    return "Patient " + patient_id + ": Low Risk";
}

int main() {
    vector<double> hemo = {13.5, 14.2, 12.8, 15.0};
    double avg, std;
    calculate_stats(&hemo, avg, std);
    cout << "Average: " << avg << ", Std Dev: " << std << endl;
    
    bool success = insert_test_result(&hemo, 14.5, 2);
    cout << "Insert Success: " << (success ? "true" : "false") << ", New list: ";
    for (double v : hemo) cout << v << " ";
    cout << endl;
    
    cout << assess_risk("P123", 220, 140, 95) << endl;
    
    return 0;
}
