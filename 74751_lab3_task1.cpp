// Lab Task 1: Patients Monitoring System
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Patient {
private:
    string bme_name;
    int bme_age;
    int bme_heart_rate;
    int bme_spo2;
    string bme_status;
    
public:
    // Constructor
    Patient(string name, int age, int heart_rate, int spo2) {
        bme_name = name;
        bme_age = age;
        bme_heart_rate = heart_rate;
        bme_spo2 = spo2;
        bme_status = "";
    }
    
    // Method to assess patient status
    string assessStatus() {
        vector<string> bme_abnormalities;
        
        // Check heart rate (normal range: 60-100 bpm)
        if (bme_heart_rate < 60) {
            bme_abnormalities.push_back("Heart rate too low: " + 
                                       to_string(bme_heart_rate) + " bpm (below 60)");
        }
        else if (bme_heart_rate > 100) {
            bme_abnormalities.push_back("Heart rate too high: " + 
                                       to_string(bme_heart_rate) + " bpm (above 100)");
        }
        
        // Check blood oxygen level (normal range: >= 95%)
        if (bme_spo2 < 95) {
            bme_abnormalities.push_back("Blood oxygen level too low: " + 
                                       to_string(bme_spo2) + "% (below 95%)");
        }
        
        // Determine status based on abnormalities
        if (!bme_abnormalities.empty()) {
            bme_status = "Critical";
            cout << "⚠️ WARNING - Patient: " << bme_name << endl;
            for (const string& bme_issue : bme_abnormalities) {
                cout << "   - " << bme_issue << endl;
            }
        }
        else {
            bme_status = "Stable";
            cout << "✅ Patient " << bme_name << " is Stable" << endl;
        }
        
        return bme_status;
    }
    
    // Method to display all patient information
    void displayInfo() {
        cout << "\n==================================================" << endl;
        cout << "PATIENT INFORMATION" << endl;
        cout << "==================================================" << endl;
        cout << "Name:           " << bme_name << endl;
        cout << "Age:            " << bme_age << " years" << endl;
        cout << "Heart Rate:     " << bme_heart_rate << " bpm" << endl;
        cout << "SpO2:           " << bme_spo2 << "%" << endl;
        cout << "Status:         " << bme_status << endl;
        cout << "==================================================" << endl;
    }
};

int main() {
    cout << "🏥 HOSPITAL VITALS MONITORING SYSTEM" << endl;
    cout << "==================================================" << endl;
    
    // Create patient objects with different combinations
    
    // Patient 1: All vitals normal
    Patient bme_patient1("Asim Munir", 45, 75, 98);
    cout << "\n[Assessing Patient 1]" << endl;
    bme_patient1.assessStatus();
    bme_patient1.displayInfo();
    
    // Patient 2: Only heart rate abnormal (tachycardia)
    Patient bme_patient2("Shahbaz Sharif", 32, 115, 97);
    cout << "\n[Assessing Patient 2]" << endl;
    bme_patient2.assessStatus();
    bme_patient2.displayInfo();
    
    // Patient 3: Multiple abnormalities (bradycardia + low SpO2)
    Patient bme_patient3("Donald Trump", 68, 52, 88);
    cout << "\n[Assessing Patient 3]" << endl;
    bme_patient3.assessStatus();
    bme_patient3.displayInfo();
    
    // Additional test: Heart rate below normal only
    Patient bme_patient4("Mariyum Nawaz", 28, 55, 96);
    cout << "\n[Assessing Patient 4]" << endl;
    bme_patient4.assessStatus();
    bme_patient4.displayInfo();
    
    return 0;
}