# Lab Task 3: Drug Dosage Calculator
class DosageCalc:
    def __init__(self, bme_weight, bme_age, bme_drug_name):
        """
        Constructor for Drug Dosage Calculator
        Stores patient weight (kg), age (years), and drug name
        """
        self.bme_weight = bme_weight
        self.bme_age = bme_age
        self.bme_drug_name = bme_drug_name
    
    def computeDose(self):
        """
        Calculates recommended dose in mg with rules:
        - Base dose: 5 mg per kg of body weight
        - Under 12 years: reduce by 30%
        - Over 65 years: reduce by 20%
        - Cap at 500 mg max
        """
        # Step 1: Calculate base dose (5 mg per kg)
        bme_base_dose = 5 * self.bme_weight
        
        # Step 2: Apply age-based reductions BEFORE checking cap
        bme_final_dose = bme_base_dose
        bme_applied_rules = []
        
        if self.bme_age < 12:
            bme_final_dose = bme_final_dose * (1 - 0.30)  # Reduce by 30%
            bme_applied_rules.append(f"Pediatric reduction (under 12): -30%")
        
        if self.bme_age > 65:
            bme_final_dose = bme_final_dose * (1 - 0.20)  # Reduce by 20%
            bme_applied_rules.append(f"Geriatric reduction (over 65): -20%")
        
        # Step 3: Apply cap if necessary (check after all reductions)
        bme_cap_applied = False
        if bme_final_dose > 500:
            bme_final_dose = 500
            bme_cap_applied = True
        
        # Store dose for other methods
        self.bme_calculated_dose = bme_final_dose
        self.bme_base_dose = bme_base_dose
        self.bme_applied_rules = bme_applied_rules
        self.bme_cap_applied = bme_cap_applied
        
        return bme_final_dose
    
    def printPrescription(self):
        """
        Displays drug name, patient details, and final dose
        """
        print("\n" + "=" * 60)
        print("💊 MEDICAL PRESCRIPTION")
        print("=" * 60)
        print(f"Drug Name:        {self.bme_drug_name}")
        print("-" * 60)
        print("PATIENT DETAILS:")
        print(f"  Weight:         {self.bme_weight} kg")
        print(f"  Age:            {self.bme_age} years")
        print("-" * 60)
        print("DOSAGE CALCULATION:")
        print(f"  Base dose:      {self.bme_base_dose:.1f} mg (5 mg/kg × {self.bme_weight} kg)")
        
        # Show applied age adjustments
        if self.bme_applied_rules:
            for bme_rule in self.bme_applied_rules:
                print(f"  {bme_rule}")
        
        # Show cap warning if applied
        if self.bme_cap_applied:
            print(f"  ⚠️  MAXIMUM DOSE CAP APPLIED: Dose > 500 mg")
        
        print(f"  ───────────────────────────")
        print(f"  FINAL DOSE:     {self.bme_calculated_dose:.1f} mg")
        
        # Safety warning for high doses
        if self.bme_calculated_dose >= 450:
            print("  ⚠️  CAUTION: Approaching maximum safe dose")
        
        print("=" * 60)


# Test the Drug Dosage Calculator
print("🏥 DRUG DOSAGE CALCULATOR - Clinical Dosing System")
print("=" * 60)

# Test Case 1: Normal adult (no adjustments, no cap)
print("\n[Test Case 1: Normal Adult]")
bme_patient1 = DosageCalc(70, 35, "Amoxicillin")
bme_patient1.computeDose()
bme_patient1.printPrescription()

# Test Case 2: Pediatric patient (under 12, 30% reduction)
print("\n[Test Case 2: Pediatric Patient - with reduction]")
bme_patient2 = DosageCalc(40, 8, "Ceftriaxone")
bme_patient2.computeDose()
bme_patient2.printPrescription()

# Test Case 3: Geriatric patient (over 65, 20% reduction)
print("\n[Test Case 3: Geriatric Patient - with reduction]")
bme_patient3 = DosageCalc(75, 72, "Warfarin")
bme_patient3.computeDose()
bme_patient3.printPrescription()

# Test Case 4: Heavy adult needing dose capping
print("\n[Test Case 4: Heavy Patient - dose cap applied]")
bme_patient4 = DosageCalc(120, 45, "Paracetamol")
bme_patient4.computeDose()
bme_patient4.printPrescription()

# Test Case 5: Pediatric patient with weight causing cap
print("\n[Test Case 5: Pediatric Patient - both pediatric reduction AND cap]")
bme_patient5 = DosageCalc(150, 10, "Ibuprofen")
bme_patient5.computeDose()
bme_patient5.printPrescription()

# Test Case 6: Elderly patient with weight causing cap
print("\n[Test Case 6: Geriatric Patient - both geriatric reduction AND cap]")
bme_patient6 = DosageCalc(130, 80, "Metformin")
bme_patient6.computeDose()
bme_patient6.printPrescription()

# Test Case 7: Very light adult (no adjustments, no cap)
print("\n[Test Case 7: Light Adult]")
bme_patient7 = DosageCalc(45, 30, "Azithromycin")
bme_patient7.computeDose()
bme_patient7.printPrescription()