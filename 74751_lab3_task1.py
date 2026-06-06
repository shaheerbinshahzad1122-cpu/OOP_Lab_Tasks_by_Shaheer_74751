# Lab Task 1: Patients Monitoring System with SQLite Database
import sqlite3
from datetime import datetime

class Patient:
    def __init__(self, bme_name, bme_age, bme_heart_rate, bme_spo2):
        """
        CONSTRUCTOR: Initializes patient object AND creates database record
        - Sets up patient attributes
        - Creates/connects to SQLite database
        - Creates tables if they don't exist
        - Saves patient data to database
        """
        # Initialize patient attributes with bme_ prefix
        self.bme_name = bme_name
        self.bme_age = bme_age
        self.bme_heart_rate = bme_heart_rate
        self.bme_spo2 = bme_spo2
        self.bme_status = None  # Will be set during assessment
        
        # ========== DATABASE SETUP (REAL SQLite) ==========
        # This creates/connects to a REAL database file on your computer
        # The file will appear in the same folder as your Python script
        self.bme_db_connection = sqlite3.connect('hospital_vitals_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        print(f"\n📁 Database connected: hospital_vitals_database.db")
        
        # Create patients table (stores current patient info)
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                heart_rate INTEGER,
                spo2 INTEGER,
                status TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        ''')
        
        # Create vital readings history table (stores all assessments)
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS vital_readings_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                heart_rate INTEGER,
                spo2 INTEGER,
                status TEXT,
                assessment_time TIMESTAMP
            )
        ''')
        
        # Insert this patient into database
        self.bme_cursor.execute('''
            INSERT INTO patients (name, age, heart_rate, spo2, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (bme_name, bme_age, bme_heart_rate, bme_spo2, 
              datetime.now(), datetime.now()))
        
        self.bme_db_connection.commit()
        self.bme_patient_id = self.bme_cursor.lastrowid
        
        print(f"✅ Patient '{bme_name}' saved to database with ID: {self.bme_patient_id}")
    
    def assessStatus(self):
        """
        Evaluates patient condition and reports all abnormalities
        Also saves the assessment results to database
        """
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
        
        # ========== UPDATE DATABASE WITH ASSESSMENT RESULTS ==========
        # Update the patient's status in the patients table
        self.bme_cursor.execute('''
            UPDATE patients 
            SET status = ?, updated_at = ?
            WHERE id = ?
        ''', (self.bme_status, datetime.now(), self.bme_patient_id))
        
        # Save this assessment to history table
        self.bme_cursor.execute('''
            INSERT INTO vital_readings_history 
            (patient_name, heart_rate, spo2, status, assessment_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.bme_name, self.bme_heart_rate, self.bme_spo2, 
              self.bme_status, datetime.now()))
        
        self.bme_db_connection.commit()
        print(f"💾 Assessment saved to database")
        
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
        print(f"Database ID:    {self.bme_patient_id}")
        print("="*50)
    
    def getPatientHistory(self):
        """
        NEW METHOD: Retrieves and displays patient's assessment history from database
        This shows how you can query data from the database
        """
        self.bme_cursor.execute('''
            SELECT assessment_time, heart_rate, spo2, status 
            FROM vital_readings_history 
            WHERE patient_name = ?
            ORDER BY assessment_time DESC
        ''', (self.bme_name,))
        
        history = self.bme_cursor.fetchall()
        
        if history:
            print(f"\n📋 ASSESSMENT HISTORY for {self.bme_name}:")
            print("-" * 50)
            for record in history:
                print(f"   Time: {record[0]}")
                print(f"   HR: {record[1]} bpm, SpO2: {record[2]}%, Status: {record[3]}")
                print("   ---")
        else:
            print(f"\n📋 No history found for {self.bme_name}")
    
    def getAllPatientsFromDatabase(self):
        """
        NEW METHOD: Shows all patients currently in the database
        Demonstrates reading from database
        """
        self.bme_cursor.execute('''
            SELECT id, name, age, heart_rate, spo2, status 
            FROM patients 
            ORDER BY created_at DESC
        ''')
        
        all_patients = self.bme_cursor.fetchall()
        
        print(f"\n📊 ALL PATIENTS IN DATABASE:")
        print("=" * 60)
        for patient in all_patients:
            print(f"   ID: {patient[0]}, Name: {patient[1]}, Age: {patient[2]}")
            print(f"   HR: {patient[3]} bpm, SpO2: {patient[4]}%, Status: {patient[5]}")
            print("   ---")
    
    def __del__(self):
        """
        DESTRUCTOR: Called automatically when object is destroyed
        - Closes the database connection properly
        - Prevents database corruption
        - Frees up system resources
        
        When is this called?
        - When you use 'del patient_object'
        - When the program ends
        - When the object goes out of scope
        """
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ DESTRUCTOR CALLED: Closing database for {self.bme_name}")
            self.bme_db_connection.close()
            print(f"   ✅ Database connection closed successfully")
            print(f"   📁 Database file: hospital_vitals_database.db")
            print(f"   💾 All patient data has been saved permanently")


# ========== MAIN PROGRAM ==========
print("=" * 60)
print("🏥 HOSPITAL VITALS MONITORING SYSTEM WITH DATABASE")
print("=" * 60)
print("\n⚠️  IMPORTANT: This program will create a REAL SQLite database file")
print("   Look for 'hospital_vitals_database.db' in the same folder")
print("=" * 60)

# Create patient objects with different combinations
print("\n1️⃣ CREATING PATIENTS (Constructor saves to database)...")
print("-" * 50)

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

# ========== DEMONSTRATE DATABASE QUERYING ==========
print("\n" + "=" * 60)
print("2️⃣ DEMONSTRATING DATABASE QUERIES")
print("=" * 60)

# Show history for one patient
bme_patient1.getPatientHistory()

# Show all patients in database
bme_patient1.getAllPatientsFromDatabase()

# ========== DEMONSTRATE DESTRUCTOR ==========
print("\n" + "=" * 60)
print("3️⃣ DEMONSTRATING DESTRUCTOR")
print("=" * 60)
print("\nManually deleting one patient to show destructor in action...")

# This will call the destructor IMMEDIATELY
del bme_patient1
print("\n✅ Patient 1 has been deleted from memory (but data remains in database!)")

print("\n" + "=" * 60)
print("4️⃣ PROGRAM ENDING")
print("=" * 60)
print("When the program ends, destructors for remaining patients will be called")
print("Look for 'hospital_vitals_database.db' in your folder!")
print("=" * 60)

# Destructors for bme_patient2, bme_patient3, bme_patient4 will be called automatically here