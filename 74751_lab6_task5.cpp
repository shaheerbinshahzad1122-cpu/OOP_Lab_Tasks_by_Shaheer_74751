// Lab Task 5: Blood Pressure Trend Analyser with Destructors
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <cmath>

using namespace std;

class BPTracker {
private:
    string bme_patient_name;
    vector<int> bme_systolic_readings;
    int bme_tracker_id;
    static int bme_next_id;
    
    string classifySingleReading(int bp) {
        if (bp < 120) return "Normal";
        else if (bp <= 129) return "Elevated";
        else return "Hypertensive";
    }
    
    void displayReadings() {
        cout << "\nRecorded Readings:" << endl;
        cout << "--------------------------------------------------" << endl;
        for (size_t i = 0; i < bme_systolic_readings.size(); i++) {
            cout << "  Day " << (i+1) << ": " << bme_systolic_readings[i] 
                 << " mmHg → " << classifySingleReading(bme_systolic_readings[i]) << endl;
        }
        cout << "--------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    BPTracker(string patient_name) {
        bme_patient_name = patient_name;
        bme_tracker_id = bme_next_id++;
        
        cout << "BP Tracker " << bme_tracker_id << " created for patient: " << bme_patient_name << endl;
    }
    
    // Method to load readings from vector
    void loadReadingsFromVector(vector<int> readings) {
        bme_systolic_readings = readings;
        displayReadings();
    }
    
    // Analysis method
    void analyse() {
        if (bme_systolic_readings.empty()) {
            cout << "\nNo readings to analyse." << endl;
            return;
        }
        
        cout << "\n============================================================" << endl;
        cout << "BLOOD PRESSURE ANALYSIS REPORT" << endl;
        cout << "Patient: " << bme_patient_name << endl;
        cout << "============================================================" << endl;
        
        // Count readings in each category
        int normal = 0, elevated = 0, hypertensive = 0;
        for (int r : bme_systolic_readings) {
            if (r < 120) normal++;
            else if (r <= 129) elevated++;
            else hypertensive++;
        }
        
        cout << "\nCATEGORY DISTRIBUTION:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Normal (<120 mmHg):        " << normal << " day(s)" << endl;
        cout << "  Elevated (120-129 mmHg):   " << elevated << " day(s)" << endl;
        cout << "  Hypertensive (≥130 mmHg):  " << hypertensive << " day(s)" << endl;
        
        // Calculate percentages
        int total = bme_systolic_readings.size();
        if (total > 0) {
            cout << "\nPercentage breakdown:" << endl;
            cout << "     Normal:      " << fixed << setprecision(1) << (normal * 100.0 / total) << "%" << endl;
            cout << "     Elevated:    " << (elevated * 100.0 / total) << "%" << endl;
            cout << "     Hypertensive: " << (hypertensive * 100.0 / total) << "%" << endl;
        }
        
        // Find highest reading
        int highest = bme_systolic_readings[0];
        int highestDay = 1;
        for (size_t i = 1; i < bme_systolic_readings.size(); i++) {
            if (bme_systolic_readings[i] > highest) {
                highest = bme_systolic_readings[i];
                highestDay = i + 1;
            }
        }
        
        cout << "\nHIGHEST READING:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Day " << highestDay << ": " << highest << " mmHg" << endl;
        
        // Check for consistently increasing trend
        bool isIncreasing = true;
        for (size_t i = 0; i < bme_systolic_readings.size() - 1; i++) {
            if (bme_systolic_readings[i + 1] <= bme_systolic_readings[i]) {
                isIncreasing = false;
                break;
            }
        }
        
        cout << "\nTREND ANALYSIS:" << endl;
        cout << "----------------------------------------" << endl;
        if (isIncreasing && bme_systolic_readings.size() > 1) {
            cout << "    WORSENING TREND DETECTED!" << endl;
            cout << "     Blood pressure increased consistently across all days." << endl;
            cout << "     Clinical follow-up recommended." << endl;
        } else {
            cout << "No consistent worsening detected." << endl;
        }
        
        // Additional statistics
        double sum = 0;
        int minVal = bme_systolic_readings[0];
        int maxVal = bme_systolic_readings[0];
        for (int r : bme_systolic_readings) {
            sum += r;
            if (r < minVal) minVal = r;
            if (r > maxVal) maxVal = r;
        }
        double avg = sum / total;
        
        cout << "\nADDITIONAL STATISTICS:" << endl;
        cout << "----------------------------------------" << endl;
        cout << "  Average BP:    " << fixed << setprecision(1) << avg << " mmHg" << endl;
        cout << "  Minimum BP:    " << minVal << " mmHg" << endl;
        cout << "  Maximum BP:    " << maxVal << " mmHg" << endl;
        cout << "  Range:         " << (maxVal - minVal) << " mmHg" << endl;
        
        // Clinical recommendations
        cout << "\nCLINICAL RECOMMENDATIONS:" << endl;
        cout << "----------------------------------------" << endl;
        
        if (hypertensive > total * 0.5) {
            cout << "URGENT: Majority of readings are in Hypertensive range." << endl;
            cout << "Immediate medical consultation required." << endl;
        } else if (hypertensive > 0) {
            cout << "CAUTION: Hypertensive readings detected." << endl;
            cout << "Schedule follow-up with cardiologist." << endl;
        }
        
        if (highest >= 180) {
            cout << "CRITICAL: Very high BP detected (≥180 mmHg)." << endl;
            cout << "Emergency evaluation may be necessary." << endl;
        } else if (highest >= 160) {
            cout << "Severe elevation detected. Prompt medical review advised." << endl;
        }
        
        if (normal == total) {
            cout << "Excellent! All readings are in normal range." << endl;
        }
        
        cout << "\n============================================================" << endl;
        cout << "End of Analysis Report" << endl;
        cout << "============================================================" << endl;
    }
    
    // DESTRUCTOR
    ~BPTracker() {
        cout << "\n DESTRUCTOR: BP Tracker " << bme_tracker_id << " for patient " << bme_patient_name << " is being destroyed" << endl;
    }
};

int BPTracker::bme_next_id = 1;

int main() {
    cout << "BLOOD PRESSURE TREND ANALYSER" << endl;
    cout << "Cardiology Department - Patient Monitoring System" << endl;
    cout << "============================================================" << endl;
    
    // Test Case 1: Worsening trend
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 1: Patient with worsening BP trend" << endl;
    cout << "============================================================" << endl;
    BPTracker bme_patient1("John Cena");
    bme_patient1.loadReadingsFromVector({118, 122, 125, 128, 131, 135});
    bme_patient1.analyse();
    
    // Test Case 2: Fluctuating BP
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 2: Patient with fluctuating BP" << endl;
    cout << "============================================================" << endl;
    BPTracker bme_patient2("Melon Husk");
    bme_patient2.loadReadingsFromVector({115, 118, 125, 122, 130, 128, 135, 132});
    bme_patient2.analyse();
    
    // Test Case 3: Normal stable BP
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 3: Patient with normal stable BP" << endl;
    cout << "============================================================" << endl;
    BPTracker bme_patient3("Gill Bates");
    bme_patient3.loadReadingsFromVector({110, 112, 115, 114, 116, 115});
    bme_patient3.analyse();
    
    // Test Case 4: Severe hypertension
    cout << "\n============================================================" << endl;
    cout << "TEST CASE 4: Patient with severe hypertension" << endl;
    cout << "============================================================" << endl;
    BPTracker bme_patient4("Mr Dogesh");
    bme_patient4.loadReadingsFromVector({145, 150, 155, 160, 158, 165, 170});
    bme_patient4.analyse();
    
    cout << "\nProgram ending - Destructors will be called automatically!" << endl;
    
    return 0;
}
