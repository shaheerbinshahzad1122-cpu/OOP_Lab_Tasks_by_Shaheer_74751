// Lab Task 5: Blood Pressure Trend Analyser
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

class BPTracker {
private:
    string bme_patient_name;
    vector<int> bme_systolic_readings;
    int bme_num_days;
    
    // Helper method to classify a single reading
    string classifySingleReading(int bme_bp) {
        if (bme_bp < 120) {
            return "Normal";
        } else if (bme_bp <= 129) {
            return "Elevated";
        } else {
            return "Hypertensive";
        }
    }
    
    // Helper to display readings
    void displayReadings() {
        cout << "\n📊 Recorded Readings:" << endl;
        cout << "--------------------------------------------------" << endl;
        for (size_t bme_i = 0; bme_i < bme_systolic_readings.size(); bme_i++) {
            string bme_status = classifySingleReading(bme_systolic_readings[bme_i]);
            cout << "  Day " << (bme_i + 1) << ": " 
                 << bme_systolic_readings[bme_i] << " mmHg → " 
                 << bme_status << endl;
        }
        cout << "--------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    BPTracker(string patient_name) {
        bme_patient_name = patient_name;
        bme_num_days = 0;
    }
    
    // Method to load readings
    void loadReadings(int bme_days) {
        bme_num_days = bme_days;
        bme_systolic_readings.clear();
        
        cout << "\n📝 Entering blood pressure readings for " << bme_patient_name << endl;
        cout << "==================================================" << endl;
        
        for (int bme_day = 1; bme_day <= bme_days; bme_day++) {
            int bme_reading;
            bool bme_valid = false;
            
            while (!bme_valid) {
                cout << "  Day " << bme_day << " - Systolic BP (mmHg): ";
                cin >> bme_reading;
                
                if (bme_reading < 50 || bme_reading > 300) {
                    cout << "    ⚠️  Warning: Unusual value! BP should be between 50-300 mmHg." << endl;
                    cout << "    Please re-enter." << endl;
                } else {
                    bme_valid = true;
                    bme_systolic_readings.push_back(bme_reading);
                }
            }
        }
        
        cout << "\n✅ All readings recorded successfully!" << endl;
        displayReadings();
    }
    
    // Method to load readings from vector (for testing)
    void loadReadingsFromVector(vector<int> bme_readings) {
        bme_systolic_readings = bme_readings;
        bme_num_days = bme_readings.size();
        displayReadings();
    }
    
    // Analysis method
    void analyse() {
        if (bme_systolic_readings.empty()) {
            cout << "\n⚠️ No readings to analyse. Please load readings first." << endl;
            return;
        }
        
        cout << "\n============================================================" << endl;
        cout << "📈 BLOOD PRESSURE ANALYSIS REPORT" << endl;
        cout << "Patient: " << bme_patient_name << endl;
        cout << "============================================================" << endl;
        
        // (a) Count readings in each category
        int bme_normal_count = 0;
        int bme_elevated_count = 0;
        int bme_hypertensive_count = 0;
        
        for (int bme_reading : bme_systolic_readings) {
            if (bme_reading < 120) {
                bme_normal_count++;
            } else if (bme_reading <= 129) {
                bme_elevated_count++;
            } else {
                bme_hypertensive_count++;
            }
        }
        
        // Display category counts
        cout << "\n📊 CATEGORY DISTRIBUTION:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Normal (<120 mmHg):        " << bme_normal_count << " day(s)" << endl;
        cout << "  Elevated (120-129 mmHg):   " << bme_elevated_count << " day(s)" << endl;
        cout << "  Hypertensive (≥130 mmHg):  " << bme_hypertensive_count << " day(s)" << endl;
        
        // Calculate percentages
        int bme_total = bme_systolic_readings.size();
        if (bme_total > 0) {
            cout << "\n  📈 Percentage breakdown:" << endl;
            cout << "     Normal:      " << fixed << setprecision(1) 
                 << (bme_normal_count * 100.0 / bme_total) << "%" << endl;
            cout << "     Elevated:    " << (bme_elevated_count * 100.0 / bme_total) << "%" << endl;
            cout << "     Hypertensive: " << (bme_hypertensive_count * 100.0 / bme_total) << "%" << endl;
        }
        
        // (b) Identify day with highest reading
        int bme_highest_value = bme_systolic_readings[0];
        int bme_highest_day = 1;
        
        for (size_t bme_i = 1; bme_i < bme_systolic_readings.size(); bme_i++) {
            if (bme_systolic_readings[bme_i] > bme_highest_value) {
                bme_highest_value = bme_systolic_readings[bme_i];
                bme_highest_day = bme_i + 1;
            }
        }
        
        cout << "\n🏆 HIGHEST READING:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Day " << bme_highest_day << ": " << bme_highest_value << " mmHg" << endl;
        
        // Check for multiple days with same highest value
        vector<int> bme_occurrences;
        for (size_t bme_i = 0; bme_i < bme_systolic_readings.size(); bme_i++) {
            if (bme_systolic_readings[bme_i] == bme_highest_value) {
                bme_occurrences.push_back(bme_i + 1);
            }
        }
        if (bme_occurrences.size() > 1) {
            cout << "  (Note: Also occurred on day(s): ";
            for (size_t bme_i = 1; bme_i < bme_occurrences.size(); bme_i++) {
                cout << bme_occurrences[bme_i];
                if (bme_i < bme_occurrences.size() - 1) cout << ", ";
            }
            cout << ")" << endl;
        }
        
        // (c) Check for consistently increasing trend
        bool bme_is_increasing = true;
        vector<pair<int, pair<int, int>>> bme_decreasing_pairs;
        
        for (size_t bme_i = 0; bme_i < bme_systolic_readings.size() - 1; bme_i++) {
            int bme_current = bme_systolic_readings[bme_i];
            int bme_next = bme_systolic_readings[bme_i + 1];
            
            if (bme_next <= bme_current) {
                bme_is_increasing = false;
                bme_decreasing_pairs.push_back({bme_i + 1, {bme_current, bme_next}});
            }
        }
        
        cout << "\n📉 TREND ANALYSIS:" << endl;
        cout << "----------------------------------------" << endl;
        
        if (bme_is_increasing && bme_systolic_readings.size() > 1) {
            cout << "  ⚠️  WORSENING TREND DETECTED!" << endl;
            cout << "     Blood pressure increased consistently across all days." << endl;
            cout << "     Clinical follow-up recommended." << endl;
        } else {
            cout << "  ✅ No consistent worsening detected." << endl;
            if (!bme_decreasing_pairs.empty()) {
                cout << "\n     Non-increasing pairs found:" << endl;
                for (size_t bme_i = 0; bme_i < bme_decreasing_pairs.size() && bme_i < 3; bme_i++) {
                    int bme_day = bme_decreasing_pairs[bme_i].first;
                    int bme_curr = bme_decreasing_pairs[bme_i].second.first;
                    int bme_next = bme_decreasing_pairs[bme_i].second.second;
                    cout << "       - Day " << bme_day << " → Day " << (bme_day + 1) 
                         << ": " << bme_curr << " → " << bme_next << " mmHg "
                         << "(" << showpos << (bme_next - bme_curr) << noshowpos << " change)" << endl;
                }
                if (bme_decreasing_pairs.size() > 3) {
                    cout << "       ... and " << (bme_decreasing_pairs.size() - 3) << " more" << endl;
                }
            }
        }
        
        // Additional statistics
        displayAdditionalStats();
        
        // Clinical recommendations
        displayRecommendations(bme_normal_count, bme_elevated_count, 
                              bme_hypertensive_count, bme_highest_value);
        
        cout << "\n============================================================" << endl;
        cout << "End of Analysis Report" << endl;
        cout << "============================================================" << endl;
    }
    
    // Display additional statistics
    void displayAdditionalStats() {
        if (bme_systolic_readings.empty()) return;
        
        double bme_sum = 0;
        int bme_min = bme_systolic_readings[0];
        int bme_max = bme_systolic_readings[0];
        
        for (int bme_val : bme_systolic_readings) {
            bme_sum += bme_val;
            if (bme_val < bme_min) bme_min = bme_val;
            if (bme_val > bme_max) bme_max = bme_val;
        }
        
        double bme_avg = bme_sum / bme_systolic_readings.size();
        int bme_range = bme_max - bme_min;
        
        // Calculate standard deviation
        double bme_variance = 0;
        for (int bme_val : bme_systolic_readings) {
            bme_variance += pow(bme_val - bme_avg, 2);
        }
        bme_variance /= bme_systolic_readings.size();
        double bme_std_dev = sqrt(bme_variance);
        
        cout << "\n📐 ADDITIONAL STATISTICS:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Average BP:    " << fixed << setprecision(1) << bme_avg << " mmHg" << endl;
        cout << "  Minimum BP:    " << bme_min << " mmHg" << endl;
        cout << "  Maximum BP:    " << bme_max << " mmHg" << endl;
        cout << "  Range:         " << bme_range << " mmHg" << endl;
        cout << "  Std Deviation: " << bme_std_dev << " mmHg" << endl;
        
        if (bme_std_dev > 15) {
            cout << "  ⚠️  High variability detected - BP is unstable" << endl;
        }
    }
    
    // Display clinical recommendations
    void displayRecommendations(int bme_normal, int bme_elevated, int bme_hypertensive, int bme_highest) {
        int bme_total = bme_systolic_readings.size();
        
        cout << "\n💡 CLINICAL RECOMMENDATIONS:" << endl;
        cout << "----------------------------------------" << endl;
        
        if (bme_hypertensive > bme_total * 0.5) {
            cout << "  🔴 URGENT: Majority of readings are in Hypertensive range." << endl;
            cout << "     Immediate medical consultation required." << endl;
        } else if (bme_hypertensive > 0) {
            cout << "  🟠 CAUTION: Hypertensive readings detected." << endl;
            cout << "     Schedule follow-up with cardiologist." << endl;
        }
        
        if (bme_elevated > bme_total * 0.3) {
            cout << "  🟡 Monitor: Elevated readings present in >30% of days." << endl;
            cout << "     Lifestyle modifications recommended." << endl;
        }
        
        if (bme_highest >= 180) {
            cout << "  🔴 CRITICAL: Very high BP detected (≥180 mmHg)." << endl;
            cout << "     Emergency evaluation may be necessary." << endl;
        } else if (bme_highest >= 160) {
            cout << "  🟠 Severe elevation detected. Prompt medical review advised." << endl;
        }
        
        if (bme_normal == bme_total) {
            cout << "  ✅ Excellent! All readings are in normal range." << endl;
            cout << "     Maintain healthy lifestyle." << endl;
        } else if (bme_normal > 0) {
            cout << "  ℹ️  Some normal readings observed. Continue monitoring." << endl;
        }
        
        cout << "  📋 General advice:" << endl;
        cout << "     - Reduce sodium intake" << endl;
        cout << "     - Regular exercise (as permitted by physician)" << endl;
        cout << "     - Stress management techniques" << endl;
        cout << "     - Regular BP monitoring" << endl;
    }
};

int main() {
    cout << "🏥 BLOOD PRESSURE TREND ANALYSER" << endl;
    cout << "Cardiology Department - Patient Monitoring System" << endl;
    cout << "============================================================" << endl;
    
    cout << "\nChoose input method:" << endl;
    cout << "1. Enter readings manually" << endl;
    cout << "2. Use demo data" << endl;
    cout << "Enter choice (1 or 2): ";
    
    int bme_choice;
    cin >> bme_choice;
    
    if (bme_choice == 1) {
        string bme_name;
        int bme_days;
        
        cout << "\nEnter patient name: ";
        cin.ignore();
        getline(cin, bme_name);
        
        BPTracker bme_patient(bme_name);
        cout << "How many days of readings? ";
        cin >> bme_days;
        
        bme_patient.loadReadings(bme_days);
        bme_patient.analyse();
    } else {
        // Demo data covering all scenarios
        cout << "\n📊 Loading demo data..." << endl;
        
        // Test Case 1: Worsening trend
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 1: Patient with worsening BP trend" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        BPTracker bme_patient1("John Cena");
        bme_patient1.loadReadingsFromVector({118, 122, 125, 128, 131, 135});
        bme_patient1.analyse();
        
        // Test Case 2: Fluctuating BP
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 2: Patient with fluctuating BP" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        BPTracker bme_patient2("Melon Husk");
        bme_patient2.loadReadingsFromVector({115, 118, 125, 122, 130, 128, 135, 132});
        bme_patient2.analyse();
        
        // Test Case 3: Normal stable BP
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 3: Patient with normal stable BP" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        BPTracker bme_patient3("Gill Bates");
        bme_patient3.loadReadingsFromVector({110, 112, 115, 114, 116, 115});
        bme_patient3.analyse();
        
        // Test Case 4: Severe hypertension
        cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        cout << "TEST CASE 4: Patient with severe hypertension" << endl;
        cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
        BPTracker bme_patient4("Dogesh Sir");
        bme_patient4.loadReadingsFromVector({145, 150, 155, 160, 158, 165, 170});
        bme_patient4.analyse();
    }
    
    return 0;
}