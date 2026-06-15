#include <iostream>
#include <string>
#include <vector>
#include <numeric>

using namespace std;

class MedicalSensor {
private:
    string sensorID;
    string type;
    double calibrationFactor;
    vector<double> recentReadings;

public:
    // Default constructor
    MedicalSensor() : sensorID("None"), type("Unknown"), calibrationFactor(1.0) {}

    // Parameterized constructor
    MedicalSensor(string id, string t, double calFactor) 
        : sensorID(id), type(t), calibrationFactor(calFactor) {}

    // Copy constructor
    MedicalSensor(const MedicalSensor& other) 
        : sensorID(other.sensorID + "_copy"), type(other.type), 
          calibrationFactor(other.calibrationFactor), recentReadings(other.recentReadings) {}

    // Destructor
    ~MedicalSensor() {
        cout << "Sensor " << sensorID << " removed from the monitoring system." << endl;
    }

    void recordReading(double value) {
        recentReadings.push_back(value);
    }

    double calculateAverage() const {
        if (recentReadings.empty()) return 0.0;
        double sum = accumulate(recentReadings.begin(), recentReadings.end(), 0.0);
        return sum / recentReadings.size();
    }

    double calculatePeak() const {
        if (recentReadings.empty()) return 0.0;
        double peak = recentReadings[0];
        for (double val : recentReadings) {
            if (val > peak) peak = val;
        }
        return peak;
    }

    void applyCalibrationAdjustment() {
        for (double& val : recentReadings) {
            val *= calibrationFactor;
        }
        cout << "Calibration applied to all recent readings." << endl;
    }

    void generateSensorReport() const {
        cout << "--- Sensor Report ---" << endl;
        cout << "ID: " << sensorID << " | Type: " << type << endl;
        cout << "Calibration Factor: " << calibrationFactor << endl;
        cout << "Number of Readings: " << recentReadings.size() << endl;
        cout << "Average Reading: " << calculateAverage() << endl;
        cout << "Peak Reading: " << calculatePeak() << endl;
    }
};

int main() {
    MedicalSensor s1("S-01", "ECG", 1.05);
    s1.recordReading(12.5);
    s1.recordReading(14.2);
    s1.recordReading(13.8);

    MedicalSensor s2 = s1; // copy

    s1.applyCalibrationAdjustment();
    s1.generateSensorReport();

    return 0;
}
