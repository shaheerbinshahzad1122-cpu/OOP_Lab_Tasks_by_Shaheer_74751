// Lab Task 4: Rehabilitation Progress Tracker
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>

using namespace std;

class RehabTracker {
private:
    int bme_num_joints;
    int bme_num_sessions;
    vector<vector<double>> bme_readings;
    int bme_tracker_id;
    static int bme_next_id;
    
public:
    // Constructor
    RehabTracker(int num_joints, int num_sessions) {
        bme_num_joints = num_joints;
        bme_num_sessions = num_sessions;
        bme_readings.assign(bme_num_joints, vector<double>(bme_num_sessions, 0));
        bme_tracker_id = bme_next_id++;
        
        cout << "Rehab Tracker " << bme_tracker_id << " created (" << bme_num_joints 
             << " joints, " << bme_num_sessions << " sessions)" << endl;
    }
    
    // Method to set readings from data
    void setReadings(vector<vector<double>> readings) {
        bme_readings = readings;
        cout << "Readings loaded into tracker" << endl;
    }
    
    // Method to display all readings
    void displayAllReadings() {
        cout << "\n============================================================" << endl;
        cout << "COMPLETE ROM READINGS TABLE" << endl;
        cout << "============================================================" << endl;
        
        cout << left << setw(10) << "Joint";
        for (int s = 0; s < bme_num_sessions; s++) {
            cout << "S" << (s+1) << setw(8);
        }
        cout << endl;
        cout << string(10 + 8 * bme_num_sessions, '-') << endl;
        
        cout << fixed << setprecision(1);
        for (int j = 0; j < bme_num_joints; j++) {
            cout << "Joint " << (j+1) << setw(5);
            for (int s = 0; s < bme_num_sessions; s++) {
                cout << bme_readings[j][s] << setw(8);
            }
            cout << endl;
        }
        cout << "============================================================" << endl;
    }
    
    // Method to analyse progress
    void analyseProgress() {
        cout << "\n============================================================" << endl;
        cout << "REHABILITATION PROGRESS ANALYSIS" << endl;
        cout << "============================================================" << endl;
        
        for (int j = 0; j < bme_num_joints; j++) {
            cout << "\n==================================================" << endl;
            cout << "JOINT " << (j + 1) << " ANALYSIS" << endl;
            cout << "==================================================" << endl;
            
            double first = bme_readings[j][0];
            double last = bme_readings[j][bme_num_sessions - 1];
            double improvement = last - first;
            
            cout << "  Initial ROM (Session 1):  " << first << "°" << endl;
            cout << "  Final ROM (Session " << bme_num_sessions << "):   " << last << "°" << endl;
            cout << "  Improvement:              " << showpos << improvement << "°" << noshowpos << endl;
            
            if (improvement > 0) {
                cout << "Progress: Improving" << endl;
            } else if (improvement < 0) {
                cout << "Progress: Declining - Needs attention!" << endl;
            } else {
                cout << "  → Progress: No change" << endl;
            }
            
            int lowCount = 0;
            cout << "\n  Session-by-session analysis:" << endl;
            
            for (int s = 0; s < bme_num_sessions; s++) {
                double reading = bme_readings[j][s];
                if (reading < 30) {
                    cout << "Session " << (s+1) << ": " << reading << "° - LOW MOBILITY WARNING!" << endl;
                    lowCount++;
                } else {
                    string status = (reading >= 60) ? "✓" : "◔";
                    cout << "    " << status << " Session " << (s+1) << ": " << reading << "°" << endl;
                }
            }
            
            if (lowCount > 0) {
                cout << "\nTotal low mobility alerts: " << lowCount << endl;
                cout << "Recommendation: Focused therapy needed for this joint" << endl;
            } else {
                cout << "\nNo low mobility issues detected" << endl;
            }
            
            if (improvement >= 15) {
                cout << "Excellent improvement! (+" << improvement << "°)" << endl;
            } else if (improvement <= -10) {
                cout << "Significant decline detected! Immediate review recommended" << endl;
            }
        }
        
        cout << "\nAnalysis complete" << endl;
    }
    
    // DESTRUCTOR
    ~RehabTracker() {
        cout << "\nDESTRUCTOR: Rehab Tracker " << bme_tracker_id << " is being destroyed" << endl;
    }
};

int RehabTracker::bme_next_id = 1;

int main() {
    cout << "REHABILITATION PROGRESS TRACKER" << endl;
    cout << "Physiotherapy Clinic - ROM Monitoring System" << endl;
    
    RehabTracker tracker(3, 4);
    
    vector<vector<double>> demoData = {
        {25, 40, 55, 70},   // Joint 1: Improving
        {45, 42, 38, 35},   // Joint 2: Declining
        {85, 88, 92, 95}    // Joint 3: Excellent
    };
    
    tracker.setReadings(demoData);
    tracker.displayAllReadings();
    tracker.analyseProgress();
    
    cout << "\nProgram ending - Destructors will be called automatically!" << endl;
    
    return 0;
}