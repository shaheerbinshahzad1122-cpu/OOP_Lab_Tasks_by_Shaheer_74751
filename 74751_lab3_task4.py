# Lab Task 4: Rehabilitation Progress Tracker with SQLite Database
import sqlite3
from datetime import datetime

class RehabTracker:
    def __init__(self, bme_num_joints, bme_num_sessions, bme_patient_name="Unknown"):
        """
        CONSTRUCTOR: Creates rehab tracker with database
        """
        self.bme_num_joints = bme_num_joints
        self.bme_num_sessions = bme_num_sessions
        self.bme_patient_name = bme_patient_name
        self.bme_readings = [[0 for _ in range(bme_num_sessions)] for _ in range(bme_num_joints)]
        
        # ========== DATABASE SETUP ==========
        self.bme_db_connection = sqlite3.connect('rehab_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        
        # Create sessions table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS rehab_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                joint_number INTEGER,
                session_number INTEGER,
                rom_reading REAL,
                recorded_at TIMESTAMP
            )
        ''')
        
        # Create progress summary table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS rehab_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                joint_number INTEGER,
                initial_rom REAL,
                final_rom REAL,
                improvement REAL,
                low_mobility_count INTEGER,
                analysis_date TIMESTAMP
            )
        ''')
        
        self.bme_db_connection.commit()
        print(f"✅ Rehabilitation database initialized for {bme_patient_name}")
    
    def enterReadings(self):
        """Accepts ROM values and saves to database"""
        print("\n" + "=" * 60)
        print("📝 ENTER RANGE-OF-MOTION (ROM) READINGS")
        print("=" * 60)
        
        for bme_joint in range(self.bme_num_joints):
            print(f"\n--- Joint {bme_joint + 1} ---")
            for bme_session in range(self.bme_num_sessions):
                while True:
                    try:
                        bme_reading = float(input(f"  Session {bme_session + 1} ROM (degrees): "))
                        if bme_reading < 0 or bme_reading > 180:
                            print("  ⚠️  ROM should be between 0° and 180°.")
                            continue
                        self.bme_readings[bme_joint][bme_session] = bme_reading
                        
                        # Save to database
                        self.bme_cursor.execute('''
                            INSERT INTO rehab_sessions 
                            (patient_name, joint_number, session_number, rom_reading, recorded_at)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (self.bme_patient_name, bme_joint + 1, bme_session + 1, 
                              bme_reading, datetime.now()))
                        self.bme_db_connection.commit()
                        
                        break
                    except ValueError:
                        print("  ⚠️  Invalid input.")
        
        print("\n✅ All readings recorded and saved to database!")
    
    def analyseProgress(self):
        """Analyses progress and saves results to database"""
        print("\n" + "=" * 60)
        print("📊 REHABILITATION PROGRESS ANALYSIS")
        print("=" * 60)
        
        for bme_joint in range(self.bme_num_joints):
            print(f"\n{'='*50}")
            print(f"🔍 JOINT {bme_joint + 1} ANALYSIS")
            print(f"{'='*50}")
            
            bme_first_reading = self.bme_readings[bme_joint][0]
            bme_last_reading = self.bme_readings[bme_joint][self.bme_num_sessions - 1]
            bme_improvement = bme_last_reading - bme_first_reading
            
            print(f"  Initial ROM:  {bme_first_reading}°")
            print(f"  Final ROM:    {bme_last_reading}°")
            print(f"  Improvement:  {bme_improvement:+.1f}°")
            
            if bme_improvement > 0:
                print(f"  ✅ Progress: Improving")
            elif bme_improvement < 0:
                print(f"  ⚠️  Progress: Declining")
            else:
                print(f"  → Progress: No change")
            
            bme_low_mobility_count = 0
            print(f"\n  Session-by-session analysis:")
            
            for bme_session in range(self.bme_num_sessions):
                bme_reading = self.bme_readings[bme_joint][bme_session]
                
                if bme_reading < 30:
                    print(f"    ⚠️  Session {bme_session + 1}: {bme_reading}° - LOW MOBILITY!")
                    bme_low_mobility_count += 1
                else:
                    bme_status = "✓" if bme_reading >= 60 else "◔"
                    print(f"    {bme_status} Session {bme_session + 1}: {bme_reading}°")
            
            # Save progress to database
            self.bme_cursor.execute('''
                INSERT INTO rehab_progress 
                (patient_name, joint_number, initial_rom, final_rom, 
                 improvement, low_mobility_count, analysis_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.bme_patient_name, bme_joint + 1, bme_first_reading, 
                  bme_last_reading, bme_improvement, bme_low_mobility_count, datetime.now()))
            self.bme_db_connection.commit()
            
            if bme_low_mobility_count > 0:
                print(f"\n  ⚠️  Total low mobility alerts: {bme_low_mobility_count}")
            else:
                print(f"\n  ✅ No low mobility issues detected")
            
            if bme_improvement >= 15:
                print(f"  🎉 Excellent improvement!")
            elif bme_improvement <= -10:
                print(f"  🚨 Significant decline detected!")
        
        print("\n" + "=" * 60)
        print("✅ Analysis complete and saved to database")
        print("=" * 60)
    
    def displayAllReadings(self):
        """Displays all readings"""
        print("\n" + "=" * 60)
        print("📋 COMPLETE ROM READINGS TABLE")
        print("=" * 60)
        
        print(f"{'Joint':<10}", end="")
        for bme_s in range(self.bme_num_sessions):
            print(f"S{bme_s+1:<8}", end="")
        print()
        print("-" * (10 + 8 * self.bme_num_sessions))
        
        for bme_joint in range(self.bme_num_joints):
            print(f"Joint {bme_joint+1:<4}", end="")
            for bme_session in range(self.bme_num_sessions):
                print(f"{self.bme_readings[bme_joint][bme_session]:<8.1f}", end="")
            print()
        print("=" * 60)
    
    def __del__(self):
        """DESTRUCTOR: Closes database connection"""
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ Closing rehabilitation database for {self.bme_patient_name}")
            self.bme_db_connection.close()
            print(f"   ✅ Database closed")


# Main program
print("🏥 REHABILITATION PROGRESS TRACKER WITH DATABASE")
print("Physiotherapy Clinic - ROM Monitoring System")

bme_tracker = RehabTracker(3, 4, "Test Patient")

print("\n" + "=" * 60)
print("Using demo data for testing...")

bme_tracker.bme_readings = [
    [25, 40, 55, 70],
    [45, 42, 38, 35],
    [85, 88, 92, 95]
]

bme_tracker.displayAllReadings()
bme_tracker.analyseProgress()

print("\n✅ All data saved to rehab_database.db")