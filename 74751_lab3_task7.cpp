// Lab Task 7: Hospital bed allocation system
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

class HospitalWard {
private:
    string bme_ward_name;
    int bme_total_beds;
    vector<string> bme_occupancy;      // "Free" or "Occupied"
    vector<string> bme_patient_names;   // Store patient names for each bed
    
    // Helper method to display ward status
    void displayWardStatus() {
        cout << "\n📋 Current Status - " << bme_ward_name << ":" << endl;
        cout << "--------------------------------------------------" << endl;
        for (int bme_i = 0; bme_i < bme_total_beds; bme_i++) {
            if (bme_occupancy[bme_i] == "Occupied") {
                cout << "  🟥 Bed " << (bme_i + 1) << ": " << bme_occupancy[bme_i]
                     << " (Patient: " << bme_patient_names[bme_i] << ")" << endl;
            } else {
                cout << "  🟩 Bed " << (bme_i + 1) << ": " << bme_occupancy[bme_i] << endl;
            }
        }
        cout << "--------------------------------------------------" << endl;
    }
    
public:
    // Constructor
    HospitalWard(string ward_name, int total_beds) {
        bme_ward_name = ward_name;
        bme_total_beds = total_beds;
        // Initialize all beds as Free
        bme_occupancy.assign(bme_total_beds, "Free");
        bme_patient_names.assign(bme_total_beds, "");
        
        cout << "✅ Ward '" << bme_ward_name << "' created with " << bme_total_beds << " beds" << endl;
        displayWardStatus();
    }
    
    // Method to admit a patient
    int admitPatient(string bme_patient_name) {
        cout << "\n🏥 ADMISSION REQUEST - Patient: " << bme_patient_name << endl;
        cout << "Ward: " << bme_ward_name << endl;
        cout << "--------------------------------------------------" << endl;
        
        // Search for first free bed
        for (int bme_bed_index = 0; bme_bed_index < bme_total_beds; bme_bed_index++) {
            if (bme_occupancy[bme_bed_index] == "Free") {
                // Found free bed - admit patient
                bme_occupancy[bme_bed_index] = "Occupied";
                bme_patient_names[bme_bed_index] = bme_patient_name;
                int bme_bed_number = bme_bed_index + 1;  // Convert to 1-indexed
                
                cout << "✅ SUCCESS: Patient " << bme_patient_name 
                     << " admitted to Bed " << bme_bed_number << endl;
                cout << "   Ward: " << bme_ward_name << endl;
                displayWardStatus();
                return bme_bed_number;
            }
        }
        
        // No free beds found
        cout << "❌ FAILED: Ward '" << bme_ward_name << "' is FULL - Cannot admit " 
             << bme_patient_name << endl;
        cout << "   All " << bme_total_beds << " beds are occupied" << endl;
        displayWardStatus();
        return -1;
    }
    
    // Method to discharge a patient
    bool dischargePatient(int bme_bed_number) {
        cout << "\n🚑 DISCHARGE REQUEST - Bed Number: " << bme_bed_number << endl;
        cout << "Ward: " << bme_ward_name << endl;
        cout << "--------------------------------------------------" << endl;
        
        // Convert to 0-indexed
        int bme_bed_index = bme_bed_number - 1;
        
        // First check: Is bed number valid?
        if (bme_bed_index < 0 || bme_bed_index >= bme_total_beds) {
            cout << "❌ ERROR: Bed " << bme_bed_number << " does not exist in '" 
                 << bme_ward_name << "'" << endl;
            cout << "   Valid bed numbers: 1 to " << bme_total_beds << endl;
            return false;
        }
        
        // Second check: Is bed currently occupied?
        if (bme_occupancy[bme_bed_index] == "Free") {
            cout << "⚠️  WARNING: Bed " << bme_bed_number << " is already FREE" << endl;
            cout << "   No patient to discharge from this bed" << endl;
            return false;
        }
        
        // Valid occupied bed - discharge patient
        string bme_discharged_patient = bme_patient_names[bme_bed_index];
        bme_occupancy[bme_bed_index] = "Free";
        bme_patient_names[bme_bed_index] = "";
        
        cout << "✅ SUCCESS: Patient " << bme_discharged_patient 
             << " discharged from Bed " << bme_bed_number << endl;
        cout << "   Bed " << bme_bed_number << " is now FREE" << endl;
        displayWardStatus();
        return true;
    }
    
    // Method to get available beds count
    int getAvailableBeds() {
        int bme_available = 0;
        for (int bme_i = 0; bme_i < bme_total_beds; bme_i++) {
            if (bme_occupancy[bme_i] == "Free") {
                bme_available++;
            }
        }
        return bme_available;
    }
    
    // Method to display ward summary
    void getWardSummary() {
        int bme_occupied = bme_total_beds - getAvailableBeds();
        double bme_percentage = (bme_occupied * 100.0) / bme_total_beds;
        
        cout << "\n📊 WARD SUMMARY - " << bme_ward_name << endl;
        cout << "   Total Beds: " << bme_total_beds << endl;
        cout << "   Occupied:   " << bme_occupied << endl;
        cout << "   Available:  " << getAvailableBeds() << endl;
        cout << "   Occupancy Rate: " << fixed << setprecision(1) << bme_percentage << "%" << endl;
    }
};

int main() {
    cout << "==================================================================" << endl;
    cout << "🏥 HOSPITAL BED ALLOCATION SYSTEM" << endl;
    cout << "Medical Administration - Ward Management" << endl;
    cout << "==================================================================" << endl;
    
    // Create two hospital wards
    cout << "\n🏗️  INITIALIZING HOSPITAL WARDS" << endl;
    cout << "==================================================================" << endl;
    HospitalWard bme_ward_a("General Medicine Ward A", 5);
    HospitalWard bme_ward_b("Surgical Ward B", 3);
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 1: Successful Admissions" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Successful admissions to Ward A
    bme_ward_a.admitPatient("Michael Jackson");
    bme_ward_a.admitPatient("Ajay Devgun");
    bme_ward_a.admitPatient("Billie Elish");
    bme_ward_a.admitPatient("Taylor Buggati");
    
    // Successful admission to Ward B
    bme_ward_b.admitPatient("Robert Wilson");
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 2: Discharge of Valid Occupied Bed" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Discharge a patient from Ward A (Bed 2)
    bme_ward_a.dischargePatient(2);
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 3: Attempt to Discharge Already-Free Bed" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Try to discharge from bed that is already free (Bed 2 again)
    bme_ward_a.dischargePatient(2);
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 4: Invalid Bed Number" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Attempt to discharge from invalid bed number
    bme_ward_a.dischargePatient(10);
    bme_ward_a.dischargePatient(0);
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 5: Fill Remaining Beds Then Overflow" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Continue admitting to fill Ward A
    bme_ward_a.admitPatient("James Bond");
    bme_ward_a.admitPatient("Ezio");
    
    // Now Ward A should be full (5/5 beds occupied)
    cout << "\n📢 Attempting admission to FULL ward:" << endl;
    bme_ward_a.admitPatient("Overflow Patient");  // Should fail - ward full
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 6: Additional Operations on Ward B" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Fill Ward B completely
    bme_ward_b.admitPatient("Arnold Shalwarnikkar");
    bme_ward_b.admitPatient("Ronnie Coleman");
    
    // Try to admit when Ward B is full
    bme_ward_b.admitPatient("Extra Patient");  // Should fail
    
    cout << "\n🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    cout << "SCENARIO 7: Discharge and Readmit" << endl;
    cout << "🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯" << endl;
    
    // Discharge a patient then readmit a new one
    bme_ward_b.dischargePatient(2);  // Discharge from Bed 2
    bme_ward_b.admitPatient("New Patient");  // Should take Bed 2
    
    cout << "\n==================================================================" << endl;
    cout << "FINAL WARD SUMMARIES" << endl;
    cout << "==================================================================" << endl;
    
    // Display final summaries
    bme_ward_a.getWardSummary();
    bme_ward_b.getWardSummary();
    
    cout << "\n==================================================================" << endl;
    cout << "🏥 Bed Allocation System Demo Complete" << endl;
    cout << "==================================================================" << endl;
    
    // Additional demonstration: Multiple ward operations
    cout << "\n🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄" << endl;
    cout << "ADVANCED SCENARIO: Cross-Ward Operations" << endl;
    cout << "🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄🔄" << endl;
    
    HospitalWard bme_ward_c("Pediatric Ward C", 2);
    bme_ward_c.admitPatient("Tommy Vercetti (age 5)");
    bme_ward_c.admitPatient("Carl Johnson (age 7)");
    
    // Try to discharge from bed 1
    bme_ward_c.dischargePatient(1);
    
    // Try to discharge from bed 1 again (already free)
    bme_ward_c.dischargePatient(1);
    
    // Bed 2 is still occupied
    bme_ward_c.getWardSummary();
    
    return 0;
}