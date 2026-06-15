#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Device {
    string name;
    double powerConsumption; // in Watts
};

class HospitalCircuit {
private:
    string circuitID;
    double voltageRating;
    double currentLoad; // in Amps
    vector<Device> connectedDevices;

public:
    // Default constructor
    HospitalCircuit() : circuitID("Unknown"), voltageRating(220.0), currentLoad(0.0) {}

    // Parameterized constructor
    HospitalCircuit(string id, double voltage) 
        : circuitID(id), voltageRating(voltage), currentLoad(0.0) {}

    // Copy constructor
    HospitalCircuit(const HospitalCircuit& other) 
        : circuitID(other.circuitID + "_copy"), voltageRating(other.voltageRating),
          currentLoad(other.currentLoad), connectedDevices(other.connectedDevices) {}

    // Destructor
    ~HospitalCircuit() {
        cout << "Circuit " << circuitID << " is taken offline." << endl;
    }

    void addDevice(string deviceName, double power) {
        connectedDevices.push_back({deviceName, power});
        currentLoad += power / voltageRating;
        cout << "Device " << deviceName << " added." << endl;
    }

    void removeDevice(string deviceName) {
        for (auto it = connectedDevices.begin(); it != connectedDevices.end(); ++it) {
            if (it->name == deviceName) {
                currentLoad -= it->powerConsumption / voltageRating;
                cout << "Device " << deviceName << " removed." << endl;
                connectedDevices.erase(it);
                return;
            }
        }
        cout << "Device not found." << endl;
    }

    double calculateTotalPowerConsumption() const {
        double totalPower = 0.0;
        for (const auto& device : connectedDevices) {
            totalPower += device.powerConsumption;
        }
        return totalPower;
    }

    bool checkForOverload(double maxCurrentLoad) const {
        return currentLoad > maxCurrentLoad;
    }

    void displayCircuitInformation() const {
        cout << "--- Circuit Information ---" << endl;
        cout << "ID: " << circuitID << " | Voltage: " << voltageRating << " V" << endl;
        cout << "Current Load: " << currentLoad << " A" << endl;
        cout << "Connected Devices: " << connectedDevices.size() << endl;
        for (const auto& device : connectedDevices) {
            cout << "  - " << device.name << " (" << device.powerConsumption << " W)" << endl;
        }
    }
};

int main() {
    HospitalCircuit c1("ICU-Wiring-01", 220.0);
    c1.addDevice("Ventilator", 500.0);
    c1.addDevice("Monitor", 100.0);
    
    HospitalCircuit c2 = c1;

    c1.displayCircuitInformation();
    cout << "Total Power Consumption: " << c1.calculateTotalPowerConsumption() << " W" << endl;
    if (c1.checkForOverload(10.0)) {
        cout << "WARNING: Overload condition detected!" << endl;
    } else {
        cout << "Circuit load is within safe limits." << endl;
    }

    c1.removeDevice("Monitor");
    
    return 0;
}
