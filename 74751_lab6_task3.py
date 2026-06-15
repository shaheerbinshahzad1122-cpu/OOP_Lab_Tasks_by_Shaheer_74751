# Lab Task 3: Drug Dosage Calculator with SQLite Database
import sqlite3
from datetime import datetime

class DosageCalc:
    def __init__(self, bme_weight, bme_age, bme_drug_name):
        """
        CONSTRUCTOR: Initializes dosage calculator with database
        """
        self.bme_weight = bme_weight
        self.bme_age = bme_age
        self.bme_drug_name = bme_drug_name
        self.bme_calculated_dose = None
        self.bme_base_dose = None
        self.bme_applied_rules = []
        self.bme_cap_applied = False
        
        # ========== DATABASE SETUP ==========
        self.bme_db_connection = sqlite3.connect('medication_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        
        # Create medication records table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS medication_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drug_name TEXT,
                patient_weight REAL,
                patient_age INTEGER,
                base_dose REAL,
                final_dose REAL,
                adjustments_applied TEXT,
                cap_applied INTEGER,
                prescribed_at TIMESTAMP
            )
        ''')
        
        # Create dosage history table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS dosage_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drug_name TEXT,
                patient_age INTEGER,
                patient_weight REAL,
                calculated_dose REAL,
                timestamp TIMESTAMP
            )
        ''')
        
        self.bme_db_connection.commit()
        print(f"✅ Medication database initialized")
    
    def computeDose(self):
        """Calculates dose and saves to database"""
        self.bme_base_dose = 5 * self.bme_weight
        bme_final_dose = self.bme_base_dose
        self.bme_applied_rules = []
        
        if self.bme_age < 12:
            bme_final_dose = bme_final_dose * 0.70
            self.bme_applied_rules.append("Pediatric reduction (-30%)")
        
        if self.bme_age > 65:
            bme_final_dose = bme_final_dose * 0.80
            self.bme_applied_rules.append("Geriatric reduction (-20%)")
        
        self.bme_cap_applied = False
        if bme_final_dose > 500:
            bme_final_dose = 500
            self.bme_cap_applied = True
            self.bme_applied_rules.append("Maximum dose cap applied (500mg)")
        
        self.bme_calculated_dose = bme_final_dose
        
        # ========== SAVE TO DATABASE ==========
        adjustments_str = ", ".join(self.bme_applied_rules) if self.bme_applied_rules else "None"
        
        self.bme_cursor.execute('''
            INSERT INTO medication_records 
            (drug_name, patient_weight, patient_age, base_dose, final_dose, 
             adjustments_applied, cap_applied, prescribed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.bme_drug_name, self.bme_weight, self.bme_age, 
              self.bme_base_dose, self.bme_calculated_dose, 
              adjustments_str, int(self.bme_cap_applied), datetime.now()))
        
        self.bme_cursor.execute('''
            INSERT INTO dosage_history (drug_name, patient_age, patient_weight, calculated_dose, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.bme_drug_name, self.bme_age, self.bme_weight, 
              self.bme_calculated_dose, datetime.now()))
        
        self.bme_db_connection.commit()
        print(f"💊 Dosage calculated and saved to database")
        
        return self.bme_calculated_dose
    
    def printPrescription(self):
        """Displays prescription"""
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
        print(f"  Base dose:      {self.bme_base_dose:.1f} mg")
        
        if self.bme_applied_rules:
            for bme_rule in self.bme_applied_rules:
                print(f"  {bme_rule}")
        
        if self.bme_cap_applied:
            print(f"  ⚠️  MAXIMUM DOSE CAP APPLIED")
        
        print(f"  ───────────────────────────")
        print(f"  FINAL DOSE:     {self.bme_calculated_dose:.1f} mg")
        
        if self.bme_calculated_dose >= 450:
            print("  ⚠️  CAUTION: Approaching maximum safe dose")
        
        print("=" * 60)
    
    def get_prescription_history(self):
        """Retrieve prescription history from database"""
        self.bme_cursor.execute('''
            SELECT drug_name, patient_weight, patient_age, final_dose, prescribed_at 
            FROM medication_records 
            ORDER BY prescribed_at DESC 
            LIMIT 5
        ''')
        history = self.bme_cursor.fetchall()
        
        print("\n📊 LAST 5 PRESCRIPTIONS:")
        for record in history:
            print(f"   {record[0]}: {record[3]}mg for {record[2]}yo/{record[1]}kg at {record[4]}")
    
    def __del__(self):
        """DESTRUCTOR: Closes database connection"""
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ Closing medication database connection")
            self.bme_db_connection.close()
            print(f"   ✅ Database closed")


# Test the Drug Dosage Calculator
print("🏥 DRUG DOSAGE CALCULATOR - WITH DATABASE")
print("=" * 60)

patients = [
    (70, 35, "Amoxicillin"),
    (40, 8, "Ceftriaxone"),
    (75, 72, "Warfarin"),
    (120, 45, "Paracetamol"),
    (150, 10, "Ibuprofen"),
    (130, 80, "Metformin"),
    (45, 30, "Azithromycin")
]

for weight, age, drug in patients:
    print(f"\n[Test Case]")
    patient = DosageCalc(weight, age, drug)
    patient.computeDose()
    patient.printPrescription()

print("\n" + "=" * 60)
print("All prescriptions saved to database")
print("=" * 60)
