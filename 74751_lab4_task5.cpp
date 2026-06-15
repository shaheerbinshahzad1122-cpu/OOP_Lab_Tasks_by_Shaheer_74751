#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<double> apply_filter(const vector<double>* original_signal, const vector<double>* filter_coefficients) {
    vector<double> filtered;
    int n = original_signal->size();
    int m = filter_coefficients->size();
    
    for (int i = 0; i < n; ++i) {
        double val = 0;
        for (int j = 0; j < m; ++j) {
            if (i - j >= 0) {
                val += (*original_signal)[i - j] * (*filter_coefficients)[j];
            }
        }
        filtered.push_back(val);
    }
    return filtered;
}

int process_log(string* log_str, string target_symptom) {
    int count = 0;
    size_t pos = 0;
    while ((pos = log_str->find(target_symptom, pos)) != string::npos) {
        count++;
        string upper_target = target_symptom;
        for (char& c : upper_target) {
            c = toupper(c);
        }
        log_str->replace(pos, target_symptom.length(), upper_target);
        pos += upper_target.length();
    }
    return count;
}

int main() {
    vector<double> sig = {1, 2, 3, 4, 5};
    vector<double> coeffs = {0.2, 0.5, 0.2};
    vector<double> filtered_sig = apply_filter(&sig, &coeffs);
    cout << "Filtered signal: ";
    for (double v : filtered_sig) cout << v << " ";
    cout << endl;
    
    string log = "headache, nausea, headache, fever";
    int count = process_log(&log, "headache");
    cout << "Count: " << count << ", Modified log: " << log << endl;
    
    return 0;
}
