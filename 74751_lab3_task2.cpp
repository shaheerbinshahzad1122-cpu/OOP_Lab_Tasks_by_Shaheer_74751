// ECG Signal Classifier
#include <iostream>
#include <string>

using namespace std;

class ECGReading {
private:
    double bme_rr_interval;    // in milliseconds
    double bme_qrs_duration;   // in milliseconds
    
public:
    // Constructor
    ECGReading(double rr_interval, double qrs_duration) {
        /*
        Boundary decisions:
        - RR interval: >= 1000ms -> Bradycardic, < 1000ms -> Normal/Tachy
        - RR interval: <= 600ms -> Tachycardic, > 600ms -> Normal/Brady
        - QRS duration: > 120ms -> Wide, <= 120ms -> Narrow
        
        Justification for boundaries:
        - RR >= 1000ms is bradycardic to include exactly 1000ms in slow heart rate
        - RR <= 600ms is tachycardic to include exactly 600ms in fast heart rate
        - QRS > 120ms is wide to classify slightly above normal as abnormal
        */
        bme_rr_interval = rr_interval;
        bme_qrs_duration = qrs_duration;
    }
    
    // Method to classify heart rhythm
    string classify() {
        string bme_rhythm_type;
        string bme_qrs_label;
        
        // First level: Classify based on RR interval (heart rate)
        if (bme_rr_interval >= 1000) {
            // Bradycardic range (slow heart rate)
            bme_rhythm_type = "Bradycardic";
            
            // Second level: Check QRS duration
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        else if (bme_rr_interval <= 600) {
            // Tachycardic range (fast heart rate)
            bme_rhythm_type = "Tachycardic";
            
            // Second level: Check QRS duration
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        else {
            // Normal range (600 < RR interval < 1000)
            bme_rhythm_type = "Normal Rhythm";
            
            // Second level: Check QRS duration
            if (bme_qrs_duration > 120) {
                bme_qrs_label = "with Wide QRS";
            } else {
                bme_qrs_label = "with Narrow QRS";
            }
        }
        
        // Construct and print the full classification
        string bme_classification = bme_rhythm_type + " " + bme_qrs_label;
        cout << "ECG Classification: " << bme_classification << endl;
        cout << "  (RR: " << bme_rr_interval << "ms, QRS: " << bme_qrs_duration << "ms)" << endl;
        
        return bme_classification;
    }
};

int main() {
    cout << "============================================================" << endl;
    cout << "🏥 ECG SIGNAL CLASSIFIER - Rhythm Analysis System" << endl;
    cout << "============================================================" << endl;
    
    // Test Case 1: Bradycardic + Narrow QRS (boundary: RR=1000ms, QRS=120ms)
    cout << "\n[Test Case 1]" << endl;
    ECGReading bme_ecg1(1000, 120);
    bme_ecg1.classify();
    
    // Test Case 2: Bradycardic + Wide QRS
    cout << "\n[Test Case 2]" << endl;
    ECGReading bme_ecg2(1100, 140);
    bme_ecg2.classify();
    
    // Test Case 3: Tachycardic + Narrow QRS (boundary: RR=600ms)
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
    
    // Test Case 7: Testing boundary at RR=601ms (just above tachycardic)
    cout << "\n[Test Case 7 - Boundary Test]" << endl;
    ECGReading bme_ecg7(601, 110);
    bme_ecg7.classify();
    
    cout << "\n============================================================" << endl;
    cout << "Classification complete - All nested branches covered" << endl;
    cout << "============================================================" << endl;
    
    return 0;
}