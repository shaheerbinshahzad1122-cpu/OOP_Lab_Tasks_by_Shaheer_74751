# Lab Task 1: Patients Monitoring system
class Patient:
    def __init__(self, bme_name, bme_age, bme_heart_rate, bme_spo2):
        # Initialize patient attributes with bme_ prefix
        self.bme_name = bme_name
        self.bme_age = bme_age
        self.bme_heart_rate = bme_heart_rate
        self.bme_spo2 = bme_spo2
        self.bme_status = None  # Will be set during assessment
    
    def assessStatus(self):
        """Evaluates patient condition and reports all abnormalities"""
        bme_abnormalities = []
        
        # Check heart rate (normal range: 60-100 bpm)
        if self.bme_heart_rate < 60:
            bme_abnormalities.append(f"Heart rate too low: {self.bme_heart_rate} bpm (below 60)")
        elif self.bme_heart_rate > 100:
            bme_abnormalities.append(f"Heart rate too high: {self.bme_heart_rate} bpm (above 100)")
        
        # Check blood oxygen level (normal range: >= 95%)
        if self.bme_spo2 < 95:
            bme_abnormalities.append(f"Blood oxygen level too low: {self.bme_spo2}% (below 95%)")
        
        # Determine status based on abnormalities
        if bme_abnormalities:
            self.bme_status = 'Critical'
            print(f"⚠️ WARNING - Patient: {self.bme_name}")
            for bme_issue in bme_abnormalities:
                print(f"   - {bme_issue}")
        else:
            self.bme_status = 'Stable'
            print(f"✅ Patient {self.bme_name} is Stable")
        
        return self.bme_status
    
    def displayInfo(self):
        """Displays all patient information with assessed status"""
        print("\n" + "="*50)
        print(f"PATIENT INFORMATION")
        print("="*50)
        print(f"Name:           {self.bme_name}")
        print(f"Age:            {self.bme_age} years")
        print(f"Heart Rate:     {self.bme_heart_rate} bpm")
        print(f"SpO2:           {self.bme_spo2}%")
        print(f"Status:         {self.bme_status}")
        print("="*50)


# Create patient objects with different combinations
print("🏥 HOSPITAL VITALS MONITORING SYSTEM")
print("="*50)

# Patient 1: All vitals normal
bme_patient1 = Patient("Asim Munir", 45, 75, 98)
print("\n[Assessing Patient 1]")
bme_patient1.assessStatus()
bme_patient1.displayInfo()

# Patient 2: Only heart rate abnormal (tachycardia)
bme_patient2 = Patient("Donald Trump", 32, 115, 97)
print("\n[Assessing Patient 2]")
bme_patient2.assessStatus()
bme_patient2.displayInfo()

# Patient 3: Multiple abnormalities (bradycardia + low SpO2)
bme_patient3 = Patient("Musa Ansari", 68, 52, 88)
print("\n[Assessing Patient 3]")
bme_patient3.assessStatus()
bme_patient3.displayInfo()

# Additional test: Heart rate below normal only
bme_patient4 = Patient("Ahmed Raza", 20, 55, 96)
print("\n[Assessing Patient 4]")
bme_patient4.assessStatus()
bme_patient4.displayInfo()