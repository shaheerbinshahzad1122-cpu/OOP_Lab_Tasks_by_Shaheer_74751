# ECG Signal Classifier with SQLite Database
import sqlite3
from datetime import datetime

class ECGReading:
    def __init__(self, bme_rr_interval, bme_qrs_duration):
        """
        CONSTRUCTOR: Initializes ECG reading AND creates database record
        - Stores RR interval and QRS duration
        - Creates/connects to SQLite database
        - Creates tables if they don't exist
        - Logs the ECG reading to database
        
        Boundary decisions:
        - RR interval: >= 1000ms -> Bradycardic, < 1000ms -> Normal/Tachy
        - RR interval: <= 600ms -> Tachycardic, > 600ms -> Normal/Brady
        - QRS duration: > 120ms -> Wide, <= 120ms -> Narrow
        """
        self.bme_rr_interval = bme_rr_interval
        self.bme_qrs_duration = bme_qrs_duration
        self.bme_classification_result = None
        
        # ========== DATABASE SETUP (REAL SQLite) ==========
        # Creates/connects to a REAL database file
        self.bme_db_connection = sqlite3.connect('ecg_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        print(f"\n📁 Database connected: ecg_database.db")
        
        # Create ECG readings table (stores all readings)
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS ecg_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rr_interval REAL,
                qrs_duration REAL,
                rhythm_type TEXT,
                qrs_label TEXT,
                classification TEXT,
                created_at TIMESTAMP
            )
        ''')
        
        # Create statistics table (for analysis)
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS ecg_statistics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_readings INTEGER,
                bradycardic_count INTEGER,
                tachycardic_count INTEGER,
                normal_count INTEGER,
                wide_qrs_count INTEGER,
                narrow_qrs_count INTEGER,
                date DATE
            )
        ''')
        
        # Create patient ECG history table (if patient name provided)
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS patient_ecg_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                rr_interval REAL,
                qrs_duration REAL,
                classification TEXT,
                recorded_at TIMESTAMP
            )
        ''')
        
        self.bme_db_connection.commit()
        print(f"✅ ECG Database initialized")
        
        # Log this reading to database (will update after classification)
        self.bme_cursor.execute('''
            INSERT INTO ecg_readings (rr_interval, qrs_duration, created_at)
            VALUES (?, ?, ?)
        ''', (bme_rr_interval, bme_qrs_duration, datetime.now()))
        
        self.bme_db_connection.commit()
        self.bme_reading_id = self.bme_cursor.lastrowid
        print(f"📊 ECG Reading {self.bme_reading_id} logged to database")
    
    def classify(self):
        """
        Classifies heart rhythm based on RR interval and QRS duration
        Also saves the classification results to database
        """
        
        # First level: Classify based on RR interval (heart rate)
        if self.bme_rr_interval >= 1000:
            # Bradycardic range (slow heart rate)
            bme_rhythm_type = "Bradycardic"
            
            # Second level: Check QRS duration
            if self.bme_qrs_duration > 120:
                bme_qrs_label = "with Wide QRS"
            else:
                bme_qrs_label = "with Narrow QRS"
                
        elif self.bme_rr_interval <= 600:
            # Tachycardic range (fast heart rate)
            bme_rhythm_type = "Tachycardic"
            
            # Second level: Check QRS duration
            if self.bme_qrs_duration > 120:
                bme_qrs_label = "with Wide QRS"
            else:
                bme_qrs_label = "with Narrow QRS"
                
        else:
            # Normal range (600 < RR interval < 1000)
            bme_rhythm_type = "Normal Rhythm"
            
            # Second level: Check QRS duration
            if self.bme_qrs_duration > 120:
                bme_qrs_label = "with Wide QRS"
            else:
                bme_qrs_label = "with Narrow QRS"
        
        # Construct the full classification
        self.bme_classification_result = f"{bme_rhythm_type} {bme_qrs_label}"
        
        # ========== SAVE CLASSIFICATION TO DATABASE ==========
        # Update the reading with classification results
        self.bme_cursor.execute('''
            UPDATE ecg_readings 
            SET rhythm_type = ?, qrs_label = ?, classification = ?
            WHERE id = ?
        ''', (bme_rhythm_type, bme_qrs_label, self.bme_classification_result, 
              self.bme_reading_id))
        
        # Update statistics
        self._update_statistics(bme_rhythm_type, bme_qrs_label)
        
        self.bme_db_connection.commit()
        print(f"💾 Classification saved to database (ID: {self.bme_reading_id})")
        
        # Print the classification
        print(f"\n🔍 ECG Classification: {self.bme_classification_result}")
        print(f"  (RR: {self.bme_rr_interval}ms, QRS: {self.bme_qrs_duration}ms)")
        
        return self.bme_classification_result
    
    def _update_statistics(self, bme_rhythm_type, bme_qrs_label):
        """
        Helper method to update statistics in database
        Called internally during classification
        """
        from datetime import date
        
        today = date.today()
        
        # Check if statistics for today exist
        self.bme_cursor.execute('''
            SELECT id, total_readings, bradycardic_count, tachycardic_count, 
                   normal_count, wide_qrs_count, narrow_qrs_count
            FROM ecg_statistics 
            WHERE date = ?
        ''', (today,))
        
        stats = self.bme_cursor.fetchone()
        
        if stats:
            # Update existing statistics
            stats_id = stats[0]
            total = stats[1] + 1
            brady_count = stats[2] + (1 if bme_rhythm_type == "Bradycardic" else 0)
            tachy_count = stats[3] + (1 if bme_rhythm_type == "Tachycardic" else 0)
            normal_count = stats[4] + (1 if bme_rhythm_type == "Normal Rhythm" else 0)
            wide_count = stats[5] + (1 if bme_qrs_label == "with Wide QRS" else 0)
            narrow_count = stats[6] + (1 if bme_qrs_label == "with Narrow QRS" else 0)
            
            self.bme_cursor.execute('''
                UPDATE ecg_statistics 
                SET total_readings = ?, bradycardic_count = ?, tachycardic_count = ?,
                    normal_count = ?, wide_qrs_count = ?, narrow_qrs_count = ?
                WHERE id = ?
            ''', (total, brady_count, tachy_count, normal_count, wide_count, 
                  narrow_count, stats_id))
        else:
            # Create new statistics for today
            self.bme_cursor.execute('''
                INSERT INTO ecg_statistics 
                (total_readings, bradycardic_count, tachycardic_count, normal_count, 
                 wide_qrs_count, narrow_qrs_count, date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (1, 
                  1 if bme_rhythm_type == "Bradycardic" else 0,
                  1 if bme_rhythm_type == "Tachycardic" else 0,
                  1 if bme_rhythm_type == "Normal Rhythm" else 0,
                  1 if bme_qrs_label == "with Wide QRS" else 0,
                  1 if bme_qrs_label == "with Narrow QRS" else 0,
                  today))
    
    def save_for_patient(self, bme_patient_name):
        """
        NEW METHOD: Save this ECG reading for a specific patient
        Links the ECG reading to a patient record
        """
        if not self.bme_classification_result:
            self.classify()  # Classify first if not done
        
        self.bme_cursor.execute('''
            INSERT INTO patient_ecg_history 
            (patient_name, rr_interval, qrs_duration, classification, recorded_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (bme_patient_name, self.bme_rr_interval, self.bme_qrs_duration,
              self.bme_classification_result, datetime.now()))
        
        self.bme_db_connection.commit()
        print(f"👤 ECG reading saved for patient: {bme_patient_name}")
    
    def get_statistics(self):
        """
        NEW METHOD: Retrieve and display statistics from database
        """
        from datetime import date
        
        self.bme_cursor.execute('''
            SELECT date, total_readings, bradycardic_count, tachycardic_count,
                   normal_count, wide_qrs_count, narrow_qrs_count
            FROM ecg_statistics 
            ORDER BY date DESC
            LIMIT 5
        ''')
        
        stats = self.bme_cursor.fetchall()
        
        if stats:
            print("\n📊 ECG STATISTICS (Last 5 Days):")
            print("=" * 60)
            for stat in stats:
                print(f"\n  Date: {stat[0]}")
                print(f"    Total Readings: {stat[1]}")
                print(f"    Bradycardic: {stat[2]}, Tachycardic: {stat[3]}, Normal: {stat[4]}")
                print(f"    Wide QRS: {stat[5]}, Narrow QRS: {stat[6]}")
        else:
            print("\n📊 No statistics available yet")
    
    def get_patient_history(self, bme_patient_name):
        """
        NEW METHOD: Get all ECG readings for a specific patient
        """
        self.bme_cursor.execute('''
            SELECT recorded_at, rr_interval, qrs_duration, classification
            FROM patient_ecg_history 
            WHERE patient_name = ?
            ORDER BY recorded_at DESC
        ''', (bme_patient_name,))
        
        history = self.bme_cursor.fetchall()
        
        if history:
            print(f"\n👤 ECG HISTORY for {bme_patient_name}:")
            print("=" * 60)
            for record in history:
                print(f"\n  Time: {record[0]}")
                print(f"    RR: {record[1]}ms, QRS: {record[2]}ms")
                print(f"    Classification: {record[3]}")
        else:
            print(f"\n👤 No ECG history found for {bme_patient_name}")
    
    def get_all_readings(self):
        """
        NEW METHOD: Display all ECG readings from database
        """
        self.bme_cursor.execute('''
            SELECT id, rr_interval, qrs_duration, classification, created_at
            FROM ecg_readings 
            ORDER BY created_at DESC
            LIMIT 10
        ''')
        
        readings = self.bme_cursor.fetchall()
        
        print("\n📋 ALL ECG READINGS IN DATABASE (Last 10):")
        print("=" * 70)
        for reading in readings:
            print(f"\n  ID: {reading[0]}")
            print(f"    RR: {reading[1]}ms, QRS: {reading[2]}ms")
            print(f"    Classification: {reading[3]}")
            print(f"    Time: {reading[4]}")
    
    def __del__(self):
        """
        DESTRUCTOR: Called automatically when object is destroyed
        - Closes the database connection properly
        - Ensures all data is saved
        - Prevents database corruption
        
        When is this called?
        - When you use 'del ecg_object'
        - When the program ends
        - When the object goes out of scope
        """
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ DESTRUCTOR CALLED: Closing ECG database")
            self.bme_db_connection.close()
            print(f"   ✅ Database connection closed successfully")
            print(f"   📁 Database file: ecg_database.db")
            print(f"   💾 All ECG readings have been saved permanently")


# ========== MAIN PROGRAM ==========
print("=" * 60)
print("🏥 ECG SIGNAL CLASSIFIER - Rhythm Analysis System WITH DATABASE")
print("=" * 60)
print("\n⚠️  IMPORTANT: This program will create a REAL SQLite database file")
print("   Look for 'ecg_database.db' in the same folder")
print("=" * 60)

print("\n1️⃣ CREATING ECG READINGS (Constructor saves to database)...")
print("-" * 50)

# Test Case 1: Bradycardic + Narrow QRS (boundary: RR=1000ms, QRS=120ms)
print("\n[Test Case 1]")
bme_ecg1 = ECGReading(1000, 120)
bme_ecg1.classify()

# Test Case 2: Bradycardic + Wide QRS
print("\n[Test Case 2]")
bme_ecg2 = ECGReading(1100, 140)
bme_ecg2.classify()

# Test Case 3: Tachycardic + Narrow QRS (boundary: RR=600ms)
print("\n[Test Case 3]")
bme_ecg3 = ECGReading(600, 80)
bme_ecg3.classify()

# Test Case 4: Tachycardic + Wide QRS
print("\n[Test Case 4]")
bme_ecg4 = ECGReading(450, 130)
bme_ecg4.classify()

# Test Case 5: Normal Rhythm + Narrow QRS
print("\n[Test Case 5]")
bme_ecg5 = ECGReading(750, 100)
bme_ecg5.classify()

# Test Case 6: Normal Rhythm + Wide QRS
print("\n[Test Case 6]")
bme_ecg6 = ECGReading(850, 125)
bme_ecg6.classify()

# Test Case 7: Testing boundary at RR=601ms (just above tachycardic)
print("\n[Test Case 7 - Boundary Test]")
bme_ecg7 = ECGReading(601, 110)
bme_ecg7.classify()

# ========== DEMONSTRATE DATABASE FEATURES ==========
print("\n" + "=" * 60)
print("2️⃣ DEMONSTRATING DATABASE FEATURES")
print("=" * 60)

# Show all readings in database
bme_ecg1.get_all_readings()

# Show statistics
bme_ecg1.get_statistics()

# Save readings for specific patients
print("\n" + "=" * 60)
print("3️⃣ SAVING READINGS FOR SPECIFIC PATIENTS")
print("=" * 60)

bme_ecg3.save_for_patient("John Smith")
bme_ecg4.save_for_patient("John Smith")
bme_ecg5.save_for_patient("Sarah Johnson")

# Get patient history
bme_ecg1.get_patient_history("John Smith")
bme_ecg1.get_patient_history("Sarah Johnson")

# ========== DEMONSTRATE DESTRUCTOR ==========
print("\n" + "=" * 60)
print("4️⃣ DEMONSTRATING DESTRUCTOR")
print("=" * 60)
print("\nManually deleting one ECG object to show destructor in action...")

# This will call the destructor IMMEDIATELY
del bme_ecg1
print("\n✅ ECG Object 1 has been deleted from memory (but data remains in database!)")

print("\n" + "=" * 60)
print("5️⃣ PROGRAM ENDING")
print("=" * 60)
print("When the program ends, destructors for remaining ECG objects will be called")
print("Look for 'ecg_database.db' in your folder!")
print("\nClassification complete - All nested branches covered")
print("=" * 60)

# Destructors for bme_ecg2 through bme_ecg7 will be called automatically here