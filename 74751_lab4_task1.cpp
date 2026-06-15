#include <iostream>
#include <vector>
#include <string>

using namespace std;

double calculate_bmi(double weight, double height) {
    return weight / (height * height);
}

void update_heart_rate(vector<int>* hr_history, int new_reading, int position) {
    if (position >= 0 && position <= hr_history->size()) {
        hr_history->insert(hr_history->begin() + position, new_reading);
    }
}

void analyze_vitals(int systolic, int diastolic, int heart_rate, string& bp_category, string& hr_status, double& map_val) {
    if (systolic > 180 || diastolic > 120) {
        bp_category = "Hypertensive Crisis";
    } else if (systolic >= 140 || diastolic >= 90) {
        bp_category = "Stage 2 Hypertension";
    } else if (systolic >= 130 || diastolic >= 80) {
        bp_category = "Stage 1 Hypertension";
    } else if (systolic >= 120 && diastolic < 80) {
        bp_category = "Elevated";
    } else {
        bp_category = "Normal";
    }

    if (heart_rate < 60) {
        hr_status = "Bradycardia";
    } else if (heart_rate > 100) {
        hr_status = "Tachycardia";
    } else {
        hr_status = "Normal";
    }

    map_val = (systolic + 2.0 * diastolic) / 3.0;
}

int main() {
    cout << "BMI: " << calculate_bmi(70, 1.75) << endl;
    
    vector<int> history = {70, 72, 75};
    update_heart_rate(&history, 80, 1);
    cout << "Updated History: ";
    for (int hr : history) cout << hr << " ";
    cout << endl;

    string bp, hr;
    double map_val;
    analyze_vitals(125, 82, 90, bp, hr, map_val);
    cout << "BP: " << bp << ", HR: " << hr << ", MAP: " << map_val << endl;
    
    return 0;
}
