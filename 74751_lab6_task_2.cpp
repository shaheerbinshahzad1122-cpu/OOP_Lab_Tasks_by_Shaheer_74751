// Lab Task 2: ECG Signal Classifier 
#include <iostream>
#include <string>

using namespace std;

class ECGReading {
private:
    double bme_rr_interval;
    double bme_qrs_duration;
    string bme_classification;
    int bme_reading_id;
    static int bme_next_id;
    
public:
    // Constructor
    ECGReading(double rr_interval, double qrs_duration) {
        bme_rr_interval = rr_interval;
        bme_qrs_duration = qrs_duration;
        bme_reading_id = bme_next_id++;
        
        cout << "ECG Reading " << bme_reading_id << " created" << endl;
    }
    
    // Method to classify heart rhythm
    string classify() {
        string bme_rhythm_type;
        string bme_qrs_label;
        
        // First level: Classify based on RR interval
        if (bme_rr_interval >= 1000) {
            bme_rhythm_type = "Bradycardic";
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        else if (bme_rr_interval <= 600) {
            bme_rhythm_type = "Tachycardic";
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        else {
            bme_rhythm_type = "Normal Rhythm";
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        
        bme_classification = bme_rhythm_type + " " + bme_qrs_label;
        
        cout << "ECG Classification: " << bme_classification << endl;
        cout << "  (RR: " << bme_rr_interval << "ms, QRS: " << bme_qrs_duration << "ms)" << endl;
        
        return bme_classification;
    }
    
    // DESTRUCTOR
    ~ECGReading() {
        cout << "\n DESTRUCTOR: ECG Reading " << bme_reading_id << " is being destroyed" << endl;
    }
};

int ECGReading::bme_next_id = 1;

int main() {
    cout << "============================================================" << endl;
    cout << "ECG SIGNAL CLASSIFIER - Rhythm Analysis System" << endl;
    cout << "============================================================" << endl;
    
    // Test Case 1: Bradycardic + Narrow QRS
    cout << "\n[Test Case 1]" << endl;
    ECGReading bme_ecg1(1000, 120);
    bme_ecg1.classify();
    
    // Test Case 2: Bradycardic + Wide QRS
    cout << "\n[Test Case 2]" << endl;
    ECGReading bme_ecg2(1100, 140);
    bme_ecg2.classify();
    
    // Test Case 3: Tachycardic + Narrow QRS
    cout << "\n[Test Case 3]" << endl;
    ECGReading bme_ecg3(600, 80);
    bme_ecg3.classify();
    
    // Test Case 4: Tachycardic + Wide QRS
    cout << "\n[Test Case 4]" << endl;
    ECGReading bme_ecg4(450, 130);
    bme_ecg4.classify();
    
    // Test Case 5: Normal Rhythm + Narrow QRS
    cout << "\n[Test Case 5]" << endl;
    ECGReading bme_ecg5(750, 100);
    bme_ecg5.classify();
    
    // Test Case 6: Normal Rhythm + Wide QRS
    cout << "\n[Test Case 6]" << endl;
    ECGReading bme_ecg6(850, 125);
    bme_ecg6.classify();
    
    // Test Case 7: Boundary test
    cout << "\n[Test Case 7 - Boundary Test]" << endl;
    ECGReading bme_ecg7(601, 110);
    bme_ecg7.classify();
    
    cout << "\nProgram ending - Destructors will be called automatically!" << endl;
    
    return 0;
}