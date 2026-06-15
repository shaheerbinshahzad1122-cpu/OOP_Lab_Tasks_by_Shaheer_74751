# Lab Task 5: Blood Pressure Trend Analyser with SQLite Database
import sqlite3
from datetime import datetime, date

class BPTracker:
    def __init__(self, bme_patient_name):
        """
        CONSTRUCTOR: Initializes BP tracker with database
        """
        self.bme_patient_name = bme_patient_name
        self.bme_systolic_readings = []
        self.bme_num_days = 0
        
        # ========== DATABASE SETUP ==========
        self.bme_db_connection = sqlite3.connect('bp_database.db')
        self.bme_cursor = self.bme_db_connection.cursor()
        
        # Create BP readings table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS bp_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                day_number INTEGER,
                systolic_bp INTEGER,
                category TEXT,
                recorded_at TIMESTAMP
            )
        ''')
        
        # Create BP analysis table
        self.bme_cursor.execute('''
            CREATE TABLE IF NOT EXISTS bp_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT,
                normal_count INTEGER,
                elevated_count INTEGER,
                hypertensive_count INTEGER,
                highest_reading INTEGER,
                highest_day INTEGER,
                worsening_trend INTEGER,
                analysis_date DATE
            )
        ''')
        
        self.bme_db_connection.commit()
        print(f"✅ BP Database initialized for {bme_patient_name}")
    
    def loadReadings(self, bme_days):
        """Accepts BP readings and saves to database"""
        self.bme_num_days = bme_days
        print(f"\n📝 Entering BP readings for {self.bme_patient_name}")
        print("=" * 50)
        
        for bme_day in range(1, bme_days + 1):
            while True:
                try:
                    bme_reading = int(input(f"  Day {bme_day} - Systolic BP (mmHg): "))
                    if bme_reading < 50 or bme_reading > 300:
                        print("    ⚠️  BP should be between 50-300 mmHg.")
                        continue
                    self.bme_systolic_readings.append(bme_reading)
                    
                    # Save to database
                    category = self._classifySingleReading(bme_reading)
                    self.bme_cursor.execute('''
                        INSERT INTO bp_readings 
                        (patient_name, day_number, systolic_bp, category, recorded_at)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (self.bme_patient_name, bme_day, bme_reading, category, datetime.now()))
                    self.bme_db_connection.commit()
                    
                    break
                except ValueError:
                    print("    ⚠️  Invalid input.")
        
        print("\n✅ All readings saved to database!")
        self._displayReadings()
    
    def _displayReadings(self):
        """Displays all readings"""
        print("\n📊 Recorded Readings:")
        print("-" * 50)
        for bme_i, bme_val in enumerate(self.bme_systolic_readings, start=1):
            bme_status = self._classifySingleReading(bme_val)
            print(f"  Day {bme_i:2d}: {bme_val:3d} mmHg → {bme_status}")
        print("-" * 50)
    
    def _classifySingleReading(self, bme_bp):
        if bme_bp < 120:
            return "Normal"
        elif bme_bp <= 129:
            return "Elevated"
        else:
            return "Hypertensive"
    
    def analyse(self):
        """Analyses BP readings and saves to database"""
        if not self.bme_systolic_readings:
            print("\n⚠️ No readings to analyse.")
            return
        
        print("\n" + "=" * 60)
        print(f"📈 BLOOD PRESSURE ANALYSIS REPORT")
        print(f"Patient: {self.bme_patient_name}")
        print("=" * 60)
        
        # Count categories
        bme_normal_count = sum(1 for r in self.bme_systolic_readings if r < 120)
        bme_elevated_count = sum(1 for r in self.bme_systolic_readings if 120 <= r <= 129)
        bme_hypertensive_count = sum(1 for r in self.bme_systolic_readings if r >= 130)
        
        print("\n📊 CATEGORY DISTRIBUTION:")
        print("-" * 40)
        print(f"  Normal (<120):        {bme_normal_count} day(s)")
        print(f"  Elevated (120-129):   {bme_elevated_count} day(s)")
        print(f"  Hypertensive (≥130):  {bme_hypertensive_count} day(s)")
        
        # Find highest reading
        bme_highest_value = max(self.bme_systolic_readings)
        bme_highest_day = self.bme_systolic_readings.index(bme_highest_value) + 1
        
        print("\n🏆 HIGHEST READING:")
        print("-" * 40)
        print(f"  Day {bme_highest_day}: {bme_highest_value} mmHg")
        
        # Check for worsening trend
        bme_is_increasing = True
        for bme_i in range(len(self.bme_systolic_readings) - 1):
            if self.bme_systolic_readings[bme_i + 1] <= self.bme_systolic_readings[bme_i]:
                bme_is_increasing = False
                break
        
        print("\n📉 TREND ANALYSIS:")
        print("-" * 40)
        if bme_is_increasing and len(self.bme_systolic_readings) > 1:
            print("  ⚠️  WORSENING TREND DETECTED!")
        else:
            print("  ✅ No consistent worsening detected.")
        
        # Save analysis to database
        self.bme_cursor.execute('''
            INSERT INTO bp_analysis 
            (patient_name, normal_count, elevated_count, hypertensive_count, 
             highest_reading, highest_day, worsening_trend, analysis_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.bme_patient_name, bme_normal_count, bme_elevated_count, 
              bme_hypertensive_count, bme_highest_value, bme_highest_day,
              1 if bme_is_increasing else 0, date.today()))
        self.bme_db_connection.commit()
        
        print("\n💾 Analysis saved to database!")
        print("=" * 60)
    
    def __del__(self):
        """DESTRUCTOR: Closes database connection"""
        if hasattr(self, 'bme_db_connection'):
            print(f"\n🗑️ Closing BP database for {self.bme_patient_name}")
            self.bme_db_connection.close()
            print(f"   ✅ Database closed")


# Main program
print("🏥 BLOOD PRESSURE TREND ANALYSER WITH DATABASE")
print("=" * 60)

# Demo data
patients_data = [
    ("Sir Zumair", [118, 122, 125, 128, 131, 135]),
    ("Sir Talha", [115, 118, 125, 122, 130, 128, 135, 132]),
    ("Dr Zeeshan", [110, 112, 115, 114, 116, 115]),
    ("Dr Jawad", [145, 150, 155, 160, 158, 165, 170])
]

for name, readings in patients_data:
    print(f"\n{'🎯'*20}")
    print(f"Patient: {name}")
    print(f"{'🎯'*20}")
    tracker = BPTracker(name)
    tracker.bme_systolic_readings = readings
    tracker.bme_num_days = len(readings)
    tracker._displayReadings()
    tracker.analyse()

print("\n✅ All BP data saved to bp_database.db")
