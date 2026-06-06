# Lab Task 7: Hospital Bed Allocation System with SQLite Database
import sqlite3
from datetime import datetime

class HospitalWard:
    def __init__(self, bme_ward_name, bme_total_beds):
        """
        CONSTRUCTOR: Creates ward and database tables
        """
        self.bme_ward_name = bme_ward_name
        self.bme_total_beds = bme_total_beds
        self.bme_occupancy = ['Free' for _ in range(bme_total_beds)]
        self.bme_patient_names = [None for _ in range(bme_total_beds)]
        
        # ========== DATABASE SETUP ==========
        self.bme_db_connection = sqlite3.connect('hospital_management.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        
        # Create wards table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS wards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ward_name TEXT UNIQUE,
                total_beds INTEGER,
                created_at TIMESTAMP
            )
        ''')
        
        # Create beds table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS beds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ward_name TEXT,
                bed_number INTEGER,
                status TEXT,
                current_patient TEXT,
                updated_at TIMESTAMP
            )
        ''')
        
        # Create admission history table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS admission_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ward_name TEXT,
                bed_number INTEGER,
                patient_name TEXT,
                action TEXT,
                action_time TIMESTAMP
            )
        ''')
        
        # Register ward
        self.bme_cursor.execute('''
            INSERT OR IGNORE INTO wards (ward_name, total_beds, created_at)
            VALUES (?, ?, ?)
        ''', (bme_ward_name, bme_total_beds, datetime.now()))
        
        # Initialize beds
        for bed_num in range(1, bme_total_beds + 1):
            self.bme_cursor.execute('''
                INSERT OR IGNORE INTO beds (ward_name, bed_number, status, updated_at)
                VALUES (?, ?, ?, ?)
            ''', (bme_ward_name, bed_num, 'Free', datetime.now()))
        
        self.bme_db_connection.commit()
        print(f"✅ Ward '{bme_ward_name}' created in database")
        self._displayWardStatus()
    
    def _displayWardStatus(self):
        """Displays current bed occupancy status"""
        print(f"\n📋 Current Status - {self.bme_ward_name}:")
        print("-" * 50)
        for bme_i in range(self.bme_total_beds):
            if self.bme_occupancy[bme_i] == 'Occupied':
                print(f"  🟥 Bed {bme_i + 1}: Occupied (Patient: {self.bme_patient_names[bme_i]})")
            else:
                print(f"  🟩 Bed {bme_i + 1}: Free")
        print("-" * 50)
    
    def admitPatient(self, bme_patient_name):
        """Admits patient and logs to database"""
        print(f"\n🏥 ADMISSION - Patient: {bme_patient_name}")
        print(f"Ward: {self.bme_ward_name}")
        print("-" * 50)
        
        for bme_bed_index in range(self.bme_total_beds):
            if self.bme_occupancy[bme_bed_index] == 'Free':
                bme_bed_number = bme_bed_index + 1
                
                self.bme_occupancy[bme_bed_index] = 'Occupied'
                self.bme_patient_names[bme_bed_index] = bme_patient_name
                
                # Update database
                self.bme_cursor.execute('''
                    UPDATE beds 
                    SET status = ?, current_patient = ?, updated_at = ?
                    WHERE ward_name = ? AND bed_number = ?
                ''', ('Occupied', bme_patient_name, datetime.now(), 
                      self.bme_ward_name, bme_bed_number))
                
                self.bme_cursor.execute('''
                    INSERT INTO admission_history 
                    (ward_name, bed_number, patient_name, action, action_time)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.bme_ward_name, bme_bed_number, bme_patient_name, 
                      'ADMITTED', datetime.now()))
                
                self.bme_db_connection.commit()
                
                print(f"✅ {bme_patient_name} admitted to Bed {bme_bed_number}")
                self._displayWardStatus()
                return bme_bed_number
        
        print(f"❌ Ward FULL - Cannot admit {bme_patient_name}")
        self._displayWardStatus()
        return None
    
    def dischargePatient(self, bme_bed_number):
        """Discharges patient and logs to database"""
        print(f"\n🚑 DISCHARGE - Bed Number: {bme_bed_number}")
        print(f"Ward: {self.bme_ward_name}")
        print("-" * 50)
        
        bme_bed_index = bme_bed_number - 1
        
        if bme_bed_index < 0 or bme_bed_index >= self.bme_total_beds:
            print(f"❌ ERROR: Bed {bme_bed_number} does not exist")
            return False
        
        if self.bme_occupancy[bme_bed_index] == 'Free':
            print(f"⚠️  Bed {bme_bed_number} is already FREE")
            return False
        
        bme_patient = self.bme_patient_names[bme_bed_index]
        self.bme_occupancy[bme_bed_index] = 'Free'
        self.bme_patient_names[bme_bed_index] = None
        
        # Update database
        self.bme_cursor.execute('''
            UPDATE beds 
            SET status = ?, current_patient = NULL, updated_at = ?
            WHERE ward_name = ? AND bed_number = ?
        ''', ('Free', datetime.now(), self.bme_ward_name, bme_bed_number))
        
        self.bme_cursor.execute('''
            INSERT INTO admission_history 
            (ward_name, bed_number, patient_name, action, action_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.bme_ward_name, bme_bed_number, bme_patient, 
              'DISCHARGED', datetime.now()))
        
        self.bme_db_connection.commit()
        
        print(f"✅ {bme_patient} discharged from Bed {bme_bed_number}")
        self._displayWardStatus()
        return True
    
    def getAvailableBeds(self):
        return self.bme_occupancy.count('Free')
    
    def getWardSummary(self):
        bme_occupied = self.bme_total_beds - self.getAvailableBeds()
        bme_percentage = (bme_occupied / self.bme_total_beds) * 100
        print(f"\n📊 WARD SUMMARY - {self.bme_ward_name}")
        print(f"   Total Beds: {self.bme_total_beds}")
        print(f"   Occupied:   {bme_occupied}")
        print(f"   Available:  {self.getAvailableBeds()}")
        print(f"   Occupancy Rate: {bme_percentage:.1f}%")
    
    def showAdmissionHistory(self):
        """Shows recent admission history"""
        self.bme_cursor.execute('''
            SELECT patient_name, action, bed_number, action_time 
            FROM admission_history 
            WHERE ward_name = ?
            ORDER BY action_time DESC 
            LIMIT 10
        ''', (self.bme_ward_name,))
        
        history = self.bme_cursor.fetchall()
        print(f"\n📋 RECENT ACTIVITY - {self.bme_ward_name}:")
        for record in history:
            print(f"   {record[0]} - {record[1]} from Bed {record[2]} at {record[3]}")
    
    def __del__(self):
        """DESTRUCTOR: Closes database connection"""
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ Closing database for ward: {self.bme_ward_name}")
            self.bme_db_connection.close()
            print(f"   ✅ Database closed")


# Main program
print("=" * 70)
print("🏥 HOSPITAL BED ALLOCATION SYSTEM WITH DATABASE")
print("=" * 70)

# Create wards
bme_ward_a = HospitalWard("General Medicine Ward A", 5)
bme_ward_b = HospitalWard("Surgical Ward B", 3)

# Admissions
bme_ward_a.admitPatient("John Smith")
bme_ward_a.admitPatient("Sarah Johnson")
bme_ward_a.admitPatient("Michael Brown")
bme_ward_a.admitPatient("Emily Davis")
bme_ward_b.admitPatient("Robert Wilson")

# Discharge
bme_ward_a.dischargePatient(2)

# Try invalid operations
bme_ward_a.dischargePatient(2)  # Already free
bme_ward_a.dischargePatient(10)  # Invalid

# Fill remaining
bme_ward_a.admitPatient("Lisa Anderson")
bme_ward_a.admitPatient("James Taylor")
bme_ward_a.admitPatient("Overflow Patient")  # Should fail

# Ward B operations
bme_ward_b.admitPatient("Maria Garcia")
bme_ward_b.admitPatient("David Lee")
bme_ward_b.admitPatient("Extra Patient")  # Should fail
bme_ward_b.dischargePatient(2)
bme_ward_b.admitPatient("New Patient")

# Show summaries
bme_ward_a.getWardSummary()
bme_ward_b.getWardSummary()

# Show history
bme_ward_a.showAdmissionHistory()

# Additional ward
bme_ward_c = HospitalWard("Pediatric Ward C", 2)
bme_ward_c.admitPatient("Tommy (age 5)")
bme_ward_c.admitPatient("Emma (age 7)")
bme_ward_c.dischargePatient(1)
bme_ward_c.dischargePatient(1)  # Already free
bme_ward_c.getWardSummary()

print("\n" + "=" * 70)
print("✅ All operations saved to hospital_management.db")
print("=" * 70)