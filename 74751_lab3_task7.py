# Lab Task 7: Hospital bed allocation system
class HospitalWard:
    def __init__(self, bme_ward_name, bme_total_beds):
        """
        Constructor for Hospital Ward
        Initializes all beds as 'Free'
        """
        self.bme_ward_name = bme_ward_name
        self.bme_total_beds = bme_total_beds
        # Initialize occupancy list: all beds start as 'Free'
        self.bme_occupancy = ['Free' for _ in range(bme_total_beds)]
        # Track patient names for each bed
        self.bme_patient_names = [None for _ in range(bme_total_beds)]
        print(f"✅ Ward '{bme_ward_name}' created with {bme_total_beds} beds")
        self._displayWardStatus()
    
    def _displayWardStatus(self):
        """Helper method to display current bed occupancy status"""
        print(f"\n📋 Current Status - {self.bme_ward_name}:")
        print("-" * 50)
        for bme_i in range(self.bme_total_beds):
            bme_status = self.bme_occupancy[bme_i]
            if bme_status == 'Occupied':
                bme_display = f"🟥 Bed {bme_i + 1}: {bme_status} (Patient: {self.bme_patient_names[bme_i]})"
            else:
                bme_display = f"🟩 Bed {bme_i + 1}: {bme_status}"
            print(f"  {bme_display}")
        print("-" * 50)
    
    def admitPatient(self, bme_patient_name):
        """
        Searches for first available free bed and admits patient
        Returns: bed number if successful, None if ward is full
        """
        print(f"\n🏥 ADMISSION REQUEST - Patient: {bme_patient_name}")
        print(f"Ward: {self.bme_ward_name}")
        print("-" * 50)
        
        # Search for first free bed
        for bme_bed_index in range(self.bme_total_beds):
            if self.bme_occupancy[bme_bed_index] == 'Free':
                # Found free bed - admit patient
                self.bme_occupancy[bme_bed_index] = 'Occupied'
                self.bme_patient_names[bme_bed_index] = bme_patient_name
                bme_bed_number = bme_bed_index + 1  # Convert to 1-indexed for display
                print(f"✅ SUCCESS: Patient {bme_patient_name} admitted to Bed {bme_bed_number}")
                print(f"   Ward: {self.bme_ward_name}")
                self._displayWardStatus()
                return bme_bed_number
        
        # No free beds found
        print(f"❌ FAILED: Ward '{self.bme_ward_name}' is FULL - Cannot admit {bme_patient_name}")
        print(f"   All {self.bme_total_beds} beds are occupied")
        self._displayWardStatus()
        return None
    
    def dischargePatient(self, bme_bed_number):
        """
        Discharges patient from specified bed number (1-indexed)
        Checks: validity first, then occupancy status
        """
        print(f"\n🚑 DISCHARGE REQUEST - Bed Number: {bme_bed_number}")
        print(f"Ward: {self.bme_ward_name}")
        print("-" * 50)
        
        # Convert to 0-indexed for internal storage
        bme_bed_index = bme_bed_number - 1
        
        # First check: Is bed number valid?
        if bme_bed_index < 0 or bme_bed_index >= self.bme_total_beds:
            print(f"❌ ERROR: Bed {bme_bed_number} does not exist in '{self.bme_ward_name}'")
            print(f"   Valid bed numbers: 1 to {self.bme_total_beds}")
            return False
        
        # Second check: Is bed currently occupied?
        if self.bme_occupancy[bme_bed_index] == 'Free':
            bme_patient = self.bme_patient_names[bme_bed_index]
            print(f"⚠️  WARNING: Bed {bme_bed_number} is already FREE")
            print(f"   No patient to discharge from this bed")
            return False
        
        # Valid occupied bed - discharge patient
        bme_discharged_patient = self.bme_patient_names[bme_bed_index]
        self.bme_occupancy[bme_bed_index] = 'Free'
        self.bme_patient_names[bme_bed_index] = None
        
        print(f"✅ SUCCESS: Patient {bme_discharged_patient} discharged from Bed {bme_bed_number}")
        print(f"   Bed {bme_bed_number} is now FREE")
        self._displayWardStatus()
        return True
    
    def getAvailableBeds(self):
        """Returns the count of available (free) beds"""
        return self.bme_occupancy.count('Free')
    
    def getWardSummary(self):
        """Prints a summary of ward occupancy"""
        bme_occupied = self.bme_total_beds - self.getAvailableBeds()
        bme_percentage = (bme_occupied / self.bme_total_beds) * 100
        print(f"\n📊 WARD SUMMARY - {self.bme_ward_name}")
        print(f"   Total Beds: {self.bme_total_beds}")
        print(f"   Occupied:   {bme_occupied}")
        print(f"   Available:  {self.getAvailableBeds()}")
        print(f"   Occupancy Rate: {bme_percentage:.1f}%")


# Main Program - Hospital Bed Allocation System
print("=" * 70)
print("🏥 HOSPITAL BED ALLOCATION SYSTEM")
print("Medical Administration - Ward Management")
print("=" * 70)

# Create two hospital wards
print("\n" + "🏗️  INITIALIZING HOSPITAL WARDS")
print("=" * 70)
bme_ward_a = HospitalWard("General Medicine Ward A", 5)
bme_ward_b = HospitalWard("Surgical Ward B", 3)

print("\n" + "🎯" * 35)
print("SCENARIO 1: Successful Admissions")
print("🎯" * 35)

# Successful admissions to Ward A
bme_ward_a.admitPatient("John Smith")
bme_ward_a.admitPatient("Sarah Johnson")
bme_ward_a.admitPatient("Michael Brown")
bme_ward_a.admitPatient("Emily Davis")

# Successful admission to Ward B
bme_ward_b.admitPatient("Robert Wilson")

print("\n" + "🎯" * 35)
print("SCENARIO 2: Discharge of Valid Occupied Bed")
print("🎯" * 35)

# Discharge a patient from Ward A (Bed 2)
bme_ward_a.dischargePatient(2)

print("\n" + "🎯" * 35)
print("SCENARIO 3: Attempt to Discharge Already-Free Bed")
print("🎯" * 35)

# Try to discharge from bed that is already free (Bed 2 again)
bme_ward_a.dischargePatient(2)

print("\n" + "🎯" * 35)
print("SCENARIO 4: Invalid Bed Number")
print("🎯" * 35)

# Attempt to discharge from invalid bed number
bme_ward_a.dischargePatient(10)
bme_ward_a.dischargePatient(0)

print("\n" + "🎯" * 35)
print("SCENARIO 5: Fill Remaining Beds Then Overflow")
print("🎯" * 35)

# Continue admitting to fill Ward A
bme_ward_a.admitPatient("Lisa Anderson")
bme_ward_a.admitPatient("James Taylor")

# Now Ward A should be full (5/5 beds occupied)
print("\n📢 Attempting admission to FULL ward:")
bme_ward_a.admitPatient("Overflow Patient")  # Should fail - ward full

print("\n" + "🎯" * 35)
print("SCENARIO 6: Additional Operations on Ward B")
print("🎯" * 35)

# Fill Ward B completely
bme_ward_b.admitPatient("Maria Garcia")
bme_ward_b.admitPatient("David Lee")

# Try to admit when Ward B is full
bme_ward_b.admitPatient("Extra Patient")  # Should fail

print("\n" + "🎯" * 35)
print("SCENARIO 7: Discharge and Readmit")
print("🎯" * 35)

# Discharge a patient then readmit a new one
bme_ward_b.dischargePatient(2)  # Discharge from Bed 2
bme_ward_b.admitPatient("New Patient")  # Should take Bed 2

print("\n" + "=" * 70)
print("FINAL WARD SUMMARIES")
print("=" * 70)

# Display final summaries
bme_ward_a.getWardSummary()
bme_ward_b.getWardSummary()

print("\n" + "=" * 70)
print("🏥 Bed Allocation System Demo Complete")
print("=" * 70)

# Additional demonstration: Multiple ward operations
print("\n" + "🔄" * 35)
print("ADVANCED SCENARIO: Cross-Ward Operations")
print("🔄" * 35)

bme_ward_c = HospitalWard("Pediatric Ward C", 2)
bme_ward_c.admitPatient("Tommy (age 5)")
bme_ward_c.admitPatient("Emma (age 7)")

# Try to discharge from bed 1
bme_ward_c.dischargePatient(1)

# Try to discharge from bed 1 again (already free)
bme_ward_c.dischargePatient(1)

# Bed 2 is still occupied
bme_ward_c.getWardSummary()