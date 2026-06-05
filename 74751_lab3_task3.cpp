// Drug Dosage Calculator
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class DosageCalc {
private:
    double bme_weight;           // in kg
    int bme_age;                 // in years
    string bme_drug_name;
    double bme_calculated_dose;
    double bme_base_dose;
    vector<string> bme_applied_rules;
    bool bme_cap_applied;
    
public:
    // Constructor
    DosageCalc(double weight, int age, string drug_name) {
        bme_weight = weight;
        bme_age = age;
        bme_drug_name = drug_name;
        bme_calculated_dose = 0;
        bme_base_dose = 0;
        bme_cap_applied = false;
    }
    
    // Method to compute the recommended dose
    double computeDose() {
        // Clear previous data
        bme_applied_rules.clear();
        bme_cap_applied = false;
        
        // Step 1: Calculate base dose (5 mg per kg)
        bme_base_dose = 5 * bme_weight;
        
        // Step 2: Apply age-based reductions BEFORE checking cap
        bme_calculated_dose = bme_base_dose;
        
        if (bme_age < 12) {
            bme_calculated_dose = bme_calculated_dose * (1 - 0.30);  // Reduce by 30%
            bme_applied_rules.push_back("Pediatric reduction (under 12): -30%");
        }
        
        if (bme_age > 65) {
            bme_calculated_dose = bme_calculated_dose * (1 - 0.20);  // Reduce by 20%
            bme_applied_rules.push_back("Geriatric reduction (over 65): -20%");
        }
        
        // Step 3: Apply cap if necessary (check after all reductions)
        if (bme_calculated_dose > 500) {
            bme_calculated_dose = 500;
            bme_cap_applied = true;
        }
        
        return bme_calculated_dose;
    }
    
    // Method to print the prescription
    void printPrescription() {
        cout << "\n============================================================" << endl;
        cout << "💊 MEDICAL PRESCRIPTION" << endl;
        cout << "============================================================" << endl;
        cout << "Drug Name:        " << bme_drug_name << endl;
        cout << "------------------------------------------------------------" << endl;
        cout << "PATIENT DETAILS:" << endl;
        cout << "  Weight:         " << bme_weight << " kg" << endl;
        cout << "  Age:            " << bme_age << " years" << endl;
        cout << "------------------------------------------------------------" << endl;
        cout << "DOSAGE CALCULATION:" << endl;
        cout << "  Base dose:      " << bme_base_dose << " mg (5 mg/kg × " << bme_weight << " kg)" << endl;
        
        // Show applied age adjustments
        for (const string& bme_rule : bme_applied_rules) {
            cout << "  " << bme_rule << endl;
        }
        
        // Show cap warning if applied
        if (bme_cap_applied) {
            cout << "  ⚠️  MAXIMUM DOSE CAP APPLIED: Dose > 500 mg" << endl;
        }
        
        cout << "  ───────────────────────────" << endl;
        cout << "  FINAL DOSE:     " << bme_calculated_dose << " mg" << endl;
        
        // Safety warning for high doses
        if (bme_calculated_dose >= 450) {
            cout << "  ⚠️  CAUTION: Approaching maximum safe dose" << endl;
        }
        
        cout << "============================================================" << endl;
    }
};

int main() {
    cout << "🏥 DRUG DOSAGE CALCULATOR - Clinical Dosing System" << endl;
    cout << "============================================================" << endl;
    
    // Test Case 1: Normal adult (no adjustments, no cap)
    cout << "\n[Test Case 1: Normal Adult]" << endl;
    DosageCalc bme_patient1(70, 35, "Amoxicillin");
    bme_patient1.computeDose();
    bme_patient1.printPrescription();
    
    // Test Case 2: Pediatric patient (under 12, 30% reduction)
    cout << "\n[Test Case 2: Pediatric Patient - with reduction]" << endl;
    DosageCalc bme_patient2(40, 8, "Ceftriaxone");
    bme_patient2.computeDose();
    bme_patient2.printPrescription();
    
    // Test Case 3: Geriatric patient (over 65, 20% reduction)
    cout << "\n[Test Case 3: Geriatric Patient - with reduction]" << endl;
    DosageCalc bme_patient3(75, 72, "Warfarin");
    bme_patient3.computeDose();
    bme_patient3.printPrescription();
    
    // Test Case 4: Heavy adult needing dose capping
    cout << "\n[Test Case 4: Heavy Patient - dose cap applied]" << endl;
    DosageCalc bme_patient4(120, 45, "Paracetamol");
    bme_patient4.computeDose();
    bme_patient4.printPrescription();
    
    // Test Case 5: Pediatric patient with weight causing cap
    // Tests both pediatric reduction AND cap condition simultaneously
    cout << "\n[Test Case 5: Pediatric Patient - both pediatric reduction AND cap]" << endl;
    DosageCalc bme_patient5(150, 10, "Ibuprofen");
    bme_patient5.computeDose();
    bme_patient5.printPrescription();
    
    // Test Case 6: Elderly patient with weight causing cap
    cout << "\n[Test Case 6: Geriatric Patient - both geriatric reduction AND cap]" << endl;
    DosageCalc bme_patient6(130, 80, "Metformin");
    bme_patient6.computeDose();
    bme_patient6.printPrescription();
    
    // Test Case 7: Very light adult (no adjustments, no cap)
    cout << "\n[Test Case 7: Light Adult]" << endl;
    DosageCalc bme_patient7(45, 30, "Azithromycin");
    bme_patient7.computeDose();
    bme_patient7.printPrescription();
    
    return 0;
}