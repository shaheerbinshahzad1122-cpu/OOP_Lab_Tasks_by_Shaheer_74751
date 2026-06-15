#include <iostream>
#include <string>

using namespace std;

class DefibrillatorModule {
private:
    string serialNumber;
    double batteryChargePercentage;
    string lastMaintenanceDate;
    double energySettings; // in Joules

public:
    // Default constructor
    DefibrillatorModule() 
        : serialNumber("UNKNOWN"), batteryChargePercentage(0.0), 
          lastMaintenanceDate("N/A"), energySettings(0.0) {}

    // Parameterized constructor
    DefibrillatorModule(string serial, double battery, string date, double energy) 
        : serialNumber(serial), batteryChargePercentage(battery), 
          lastMaintenanceDate(date), energySettings(energy) {}

    // Copy constructor
    DefibrillatorModule(const DefibrillatorModule& other) 
        : serialNumber(other.serialNumber + "_copy"), 
          batteryChargePercentage(other.batteryChargePercentage), 
          lastMaintenanceDate(other.lastMaintenanceDate), 
          energySettings(other.energySettings) {}

    // Destructor
    ~DefibrillatorModule() {
        cout << "Device Deactivation Log: Defibrillator " << serialNumber << " is going offline." << endl;
    }

    void updateBatteryCharge(double amount) {
        batteryChargePercentage += amount;
        if (batteryChargePercentage > 100.0) batteryChargePercentage = 100.0;
        if (batteryChargePercentage < 0.0) batteryChargePercentage = 0.0;
        cout << "Battery charge updated to " << batteryChargePercentage << "%" << endl;
    }

    void setEnergyLevel(double level) {
        energySettings = level;
        cout << "Energy level set to " << energySettings << " Joules." << endl;
    }

    void performSelfTest() const {
        cout << "Performing self-test on Defibrillator " << serialNumber << "..." << endl;
        if (batteryChargePercentage > 20.0) {
            cout << "Self-test passed. Device is ready." << endl;
        } else {
            cout << "Self-test failed. Battery too low!" << endl;
        }
    }

    int calculateEstimatedRemainingUses() const {
        // Assume each use at current energy setting consumes (energySettings / 100) % of battery
        // Or simple estimation: 1 use consumes 5% of battery if energy is > 0
        if (energySettings <= 0) return 0;
        
        double consumePerUse = (energySettings / 200.0) * 5.0; // dummy formula
        if (consumePerUse <= 0) consumePerUse = 1.0;
        
        return static_cast<int>(batteryChargePercentage / consumePerUse);
    }
};

int main() {
    DefibrillatorModule d1("DEF-9901", 100.0, "2023-10-01", 150.0);
    DefibrillatorModule d2 = d1;
    
    d1.performSelfTest();
    d1.updateBatteryCharge(-30.0);
    d1.setEnergyLevel(200.0);
    
    cout << "Estimated remaining uses: " << d1.calculateEstimatedRemainingUses() << endl;
    
    return 0;
}
