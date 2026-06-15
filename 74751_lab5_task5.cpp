#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

class PatientMonitor {
private:
    string monitorID;
    string patientID;
    map<string, vector<double>> vitalSignals;

public:
    // Default constructor
    PatientMonitor() : monitorID("UNKNOWN"), patientID("UNKNOWN") {}

    // Parameterized constructor
    PatientMonitor(string mID, string pID) : monitorID(mID), patientID(pID) {}

    // Deep-copy constructor
    PatientMonitor(const PatientMonitor& other) 
        : monitorID(other.monitorID + "_copy"), patientID(other.patientID) {
        for (const auto& pair : other.vitalSignals) {
            vitalSignals[pair.first] = vector<double>(pair.second);
        }
    }

    // Destructor
    ~PatientMonitor() {
        cout << "Patient Monitor " << monitorID << " detached from patient " << patientID << "." << endl;
    }

    void addSignalSample(string channel, double value) {
        vitalSignals[channel].push_back(value);
    }

    double computeAverage(string channel) const {
        auto it = vitalSignals.find(channel);
        if (it != vitalSignals.end() && !it->second.empty()) {
            double sum = accumulate(it->second.begin(), it->second.end(), 0.0);
            return sum / it->second.size();
        }
        return 0.0;
    }

    void detectAbnormalReadings(string channel, double minSafe, double maxSafe) const {
        auto it = vitalSignals.find(channel);
        if (it != vitalSignals.end()) {
            for (double val : it->second) {
                if (val < minSafe || val > maxSafe) {
                    cout << "ALERT: Abnormal reading " << val << " detected on channel " << channel << "!" << endl;
                }
            }
        }
    }

    void produceMonitoringSummaryReport() const {
        cout << "--- Monitoring Summary Report ---" << endl;
        cout << "Monitor ID: " << monitorID << " | Patient ID: " << patientID << endl;
        for (const auto& pair : vitalSignals) {
            cout << "Channel: " << pair.first << endl;
            cout << "  - Samples: " << pair.second.size() << endl;
            double sum = accumulate(pair.second.begin(), pair.second.end(), 0.0);
            double avg = pair.second.empty() ? 0.0 : sum / pair.second.size();
            cout << "  - Average: " << avg << endl;
        }
        cout << "---------------------------------" << endl;
    }
};

int main() {
    PatientMonitor p1("PM-01", "PT-1234");
    p1.addSignalSample("HeartRate", 75.0);
    p1.addSignalSample("HeartRate", 78.0);
    p1.addSignalSample("HeartRate", 120.0); // Abnormal
    
    p1.addSignalSample("Voltage", 12.1);
    p1.addSignalSample("Voltage", 11.9);

    PatientMonitor p2 = p1; // Deep copy
    
    p1.detectAbnormalReadings("HeartRate", 60.0, 100.0);
    p1.produceMonitoringSummaryReport();

    return 0;
}
