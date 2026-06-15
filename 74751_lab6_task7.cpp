// Lab Task 7: Hospital Bed Allocation System with Destructors
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

class HospitalWard {
private:
    string bme_ward_name;
    int bme_total_beds;
    vector<string> bme_occupancy;
    vector<string> bme_patient_names;
    int bme_ward_id;
    static int bme_next_id;
    
    void displayWardStatus() {
        cout << "\nCurrent Status - " << bme_ward_name << ":" << endl;
        cout << "--------------------------------------------------" << endl;
        for (int i = 0; i < bme_total_beds; i++) {
            if (bme_occupancy[i] == "Occupied") {
                cout << "   Bed " << (i + 1) << ": Occupied (Patient: " << bme_patient_names[i] << ")" << endl;
            } else {
                cout << "   Bed " << (i + 1) << ": Free" << endl;
            }
        }
        cout << "--------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    HospitalWard(string ward_name, int total_beds) {
        bme_ward_name = ward_name;
        bme_total_beds = total_beds;
        bme_occupancy.assign(bme_total_beds, "Free");
        bme_patient_names.assign(bme_total_beds, "");
        bme_ward_id = bme_next_id++;
        
        cout << " Ward '" << bme_ward_name << "' created with " << bme_total_beds << " beds" << endl;
        displayWardStatus();
    }
    
    // Method to admit a patient
    int admitPatient(string bme_patient_name) {
        cout << "\n ADMISSION REQUEST - Patient: " << bme_patient_name << endl;
        cout << "Ward: " << bme_ward_name << endl;
        cout << "--------------------------------------------------" << endl;
        
        for (int i = 0; i < bme_total_beds; i++) {
            if (bme_occupancy[i] == "Free") {
                bme_occupancy[i] = "Occupied";
                bme_patient_names[i] = bme_patient_name;
                int bedNum = i + 1;
                
                cout << " SUCCESS: Patient " << bme_patient_name << " admitted to Bed " << bedNum << endl;
                displayWardStatus();
                return bedNum;
            }
        }
        
        cout << " FAILED: Ward '" << bme_ward_name << "' is FULL - Cannot admit " << bme_patient_name << endl;
        cout << "   All " << bme_total_beds << " beds are occupied" << endl;
        displayWardStatus();
        return -1;
    }
    
    // Method to discharge a patient
    bool dischargePatient(int bme_bed_number) {
        cout << "\n DISCHARGE REQUEST - Bed Number: " << bme_bed_number << endl;
        cout << "Ward: " << bme_ward_name << endl;
        cout << "--------------------------------------------------" << endl;
        
        int index = bme_bed_number - 1;
        
        // First check: Is bed number valid?
        if (index < 0 || index >= bme_total_beds) {
            cout << " ERROR: Bed " << bme_bed_number << " does not exist in '" << bme_ward_name << "'" << endl;
            cout << "   Valid bed numbers: 1 to " << bme_total_beds << endl;
            return false;
        }
        
        // Second check: Is bed currently occupied?
        if (bme_occupancy[index] == "Free") {
            cout << "  WARNING: Bed " << bme_bed_number << " is already FREE" << endl;
            cout << "   No patient to discharge from this bed" << endl;
            return false;
        }
        
        // Valid occupied bed - discharge patient
        string discharged = bme_patient_names[index];
        bme_occupancy[index] = "Free";
        bme_patient_names[index] = "";
        
        cout << " SUCCESS: Patient " << discharged << " discharged from Bed " << bme_bed_number << endl;
        cout << "   Bed " << bme_bed_number << " is now FREE" << endl;
        displayWardStatus();
        return true;
    }
    
    // Method to get available beds count
    int getAvailableBeds() {
        int available = 0;
        for (int i = 0; i < bme_total_beds; i++) {
            if (bme_occupancy[i] == "Free") available++;
        }
        return available;
    }
    
    // Method to display ward summary
    void getWardSummary() {
        int occupied = bme_total_beds - getAvailableBeds();
        double percentage = (occupied * 100.0) / bme_total_beds;
        
        cout << "\n WARD SUMMARY - " << bme_ward_name << endl;
        cout << "   Total Beds: " << bme_total_beds << endl;
        cout << "   Occupied:   " << occupied << endl;
        cout << "   Available:  " << getAvailableBeds() << endl;
        cout << "   Occupancy Rate: " << fixed << setprecision(1) << percentage << "%" << endl;
    }
    
    // DESTRUCTOR
    ~HospitalWard() {
        cout << "\n DESTRUCTOR: Ward " << bme_ward_id << " ('" << bme_ward_name << "') is being destroyed" << endl;
    }
};

int HospitalWard::bme_next_id = 1;

int main() {
    cout << "==================================================================" << endl;
    cout << " HOSPITAL BED ALLOCATION SYSTEM" << endl;
    cout << "Medical Administration - Ward Management" << endl;
    cout << "==================================================================" << endl;
    
    // Create wards
    cout << "\n  INITIALIZING HOSPITAL WARDS" << endl;
    cout << "==================================================================" << endl;
    HospitalWard bme_ward_a("General Medicine Ward A", 5);
    HospitalWard bme_ward_b("Surgical Ward B", 3);
    
    // SCENARIO 1: Successful Admissions
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 1: Successful Admissions" << endl;
    cout << "==================================================================" << endl;
    
    bme_ward_a.admitPatient("Michael Jackson");
    bme_ward_a.admitPatient("Ajay Devgun");
    bme_ward_a.admitPatient("Billie Elish");
    bme_ward_a.admitPatient("Taylor Buggati");
    bme_ward_b.admitPatient("Robert Wilson");
    
    // SCENARIO 2: Discharge of Valid Occupied Bed
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 2: Discharge of Valid Occupied Bed" << endl;
    cout << "==================================================================" << endl;
    bme_ward_a.dischargePatient(2);
    
    // SCENARIO 3: Attempt to Discharge Already-Free Bed
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 3: Attempt to Discharge Already-Free Bed" << endl;
    cout << "==================================================================" << endl;
    bme_ward_a.dischargePatient(2);
    
    // SCENARIO 4: Invalid Bed Number
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 4: Invalid Bed Number" << endl;
    cout << "==================================================================" << endl;
    bme_ward_a.dischargePatient(10);
    bme_ward_a.dischargePatient(0);
    
    // SCENARIO 5: Fill Remaining Beds Then Overflow
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 5: Fill Remaining Beds Then Overflow" << endl;
    cout << "==================================================================" << endl;
    
    bme_ward_a.admitPatient("James Bond");
    bme_ward_a.admitPatient("Ezio");
    
    cout << "\n Attempting admission to FULL ward:" << endl;
    bme_ward_a.admitPatient("Overflow Patient");
    
    // SCENARIO 6: Additional Operations on Ward B
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 6: Additional Operations on Ward B" << endl;
    cout << "==================================================================" << endl;
    
    bme_ward_b.admitPatient("Arnold Shalwarnikkar");
    bme_ward_b.admitPatient("Ronnie Coleman");
    bme_ward_b.admitPatient("Extra Patient");
    
    // SCENARIO 7: Discharge and Readmit
    cout << "\n==================================================================" << endl;
    cout << "SCENARIO 7: Discharge and Readmit" << endl;
    cout << "==================================================================" << endl;
    
    bme_ward_b.dischargePatient(2);
    bme_ward_b.admitPatient("New Patient");
    
    // Final Summaries
    cout << "\n==================================================================" << endl;
    cout << "FINAL WARD SUMMARIES" << endl;
    cout << "==================================================================" << endl;
    bme_ward_a.getWardSummary();
    bme_ward_b.getWardSummary();
    
    // Cross-Ward Operations
    cout << "\n🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄" << endl;
    cout << "ADVANCED SCENARIO: Cross-Ward Operations" << endl;
    cout << "🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄" << endl;
    
    HospitalWard bme_ward_c("Pediatric Ward C", 2);
    bme_ward_c.admitPatient("Tommy Vercetti (age 5)");
    bme_ward_c.admitPatient("Carl Johnson (age 7)");
    bme_ward_c.dischargePatient(1);
    bme_ward_c.dischargePatient(1);
    bme_ward_c.getWardSummary();
    
    cout << "\nProgram ending - Destructors will be called automatically!" << endl;
    
    return 0;
}
