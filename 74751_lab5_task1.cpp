#include <iostream>
#include <string>

using namespace std;

class BatteryBackup {
private:
    string batteryID;
    double capacity;
    double currentChargeLevel;
    double voltage;

public:
    // Default constructor
    BatteryBackup() : batteryID("Unknown"), capacity(0.0), currentChargeLevel(0.0), voltage(0.0) {}

    // Parameterized constructor
    BatteryBackup(string id, double cap, double vol) 
        : batteryID(id), capacity(cap), currentChargeLevel(cap), voltage(vol) {}

    // Copy constructor
    BatteryBackup(const BatteryBackup& other) 
        : batteryID(other.batteryID + "_copy"), capacity(other.capacity), 
          currentChargeLevel(other.currentChargeLevel), voltage(other.voltage) {}

    // Destructor
    ~BatteryBackup() {
        cout << "System shutdown log: BatteryBackup object " << batteryID << " is being destroyed." << endl;
    }

    void chargeBattery(double amount) {
        if (amount > 0) {
            currentChargeLevel += amount;
            if (currentChargeLevel > capacity) {
                currentChargeLevel = capacity;
            }
            cout << "Battery charged. Current level: " << currentChargeLevel << " Ah" << endl;
        }
    }

    void discharge(double amount) {
        if (amount > 0) {
            if (currentChargeLevel >= amount) {
                currentChargeLevel -= amount;
                cout << "Discharged " << amount << " Ah. Remaining: " << currentChargeLevel << " Ah" << endl;
            } else {
                cout << "Safety Check Failed: Insufficient charge for this discharge amount." << endl;
            }
        }
    }

    double calculateRemainingBackupTime(double currentLoad) const {
        if (currentLoad > 0) {
            return currentChargeLevel / currentLoad; // Hours remaining
        }
        return 0.0;
    }

    void displayStatus() const {
        cout << "--- Battery Status ---" << endl;
        cout << "ID: " << batteryID << endl;
        cout << "Capacity: " << capacity << " Ah" << endl;
        cout << "Current Charge Level: " << currentChargeLevel << " Ah" << endl;
        cout << "Voltage: " << voltage << " V" << endl;
    }
};

int main() {
    BatteryBackup defaultBattery;
    BatteryBackup b1("UPS-101", 100.0, 12.0);
    BatteryBackup b2 = b1; // Copy constructor

    b1.displayStatus();
    b1.discharge(20.0);
    b1.discharge(100.0); // Safety check
    b1.chargeBattery(10.0);
    cout << "Remaining backup time at 5A load: " << b1.calculateRemainingBackupTime(5.0) << " hours" << endl;

    return 0;
}
