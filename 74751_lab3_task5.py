# Lab Task 5: Blood Pressure Trend Analyser
class BPTracker:
    def __init__(self, bme_patient_name):
        """
        Constructor for Blood Pressure Tracker
        Stores patient name and initializes empty list for BP readings
        """
        self.bme_patient_name = bme_patient_name
        self.bme_systolic_readings = []  # List to store BP readings
        self.bme_num_days = 0
    
    def loadReadings(self, bme_days):
        """
        Accepts 'days' number of systolic readings from user
        Uses a loop to collect each day's reading
        """
        self.bme_num_days = bme_days
        print(f"\n📝 Entering blood pressure readings for {self.bme_patient_name}")
        print("=" * 50)
        
        for bme_day in range(1, bme_days + 1):
            while True:  # Input validation loop
                try:
                    bme_reading = int(input(f"  Day {bme_day} - Systolic BP (mmHg): "))
                    if bme_reading < 50 or bme_reading > 300:
                        print("    ⚠️  Warning: Unusual value! BP should be between 50-300 mmHg.")
                        print("    Please re-enter.")
                        continue
                    self.bme_systolic_readings.append(bme_reading)
                    break
                except ValueError:
                    print("    ⚠️  Invalid input. Please enter a whole number.")
        
        print("\n✅ All readings recorded successfully!")
        self._displayReadings()
    
    def _displayReadings(self):
        """Helper method to display all entered readings"""
        print("\n📊 Recorded Readings:")
        print("-" * 50)
        for bme_i, bme_val in enumerate(self.bme_systolic_readings, start=1):
            bme_status = self._classifySingleReading(bme_val)
            print(f"  Day {bme_i:2d}: {bme_val:3d} mmHg → {bme_status}")
        print("-" * 50)
    
    def _classifySingleReading(self, bme_bp):
        """Helper to classify a single BP reading"""
        if bme_bp < 120:
            return "Normal"
        elif bme_bp <= 129:
            return "Elevated"
        else:
            return "Hypertensive"
    
    def analyse(self):
        """
        Analyses BP readings:
        (a) Counts readings in each category
        (b) Identifies day with highest reading
        (c) Checks for consistently increasing trend
        """
        if not self.bme_systolic_readings:
            print("\n⚠️ No readings to analyse. Please load readings first.")
            return
        
        print("\n" + "=" * 60)
        print(f"📈 BLOOD PRESSURE ANALYSIS REPORT")
        print(f"Patient: {self.bme_patient_name}")
        print("=" * 60)
        
        # (a) Count readings in each category
        bme_normal_count = 0
        bme_elevated_count = 0
        bme_hypertensive_count = 0
        
        for bme_reading in self.bme_systolic_readings:
            if bme_reading < 120:
                bme_normal_count += 1
            elif bme_reading <= 129:
                bme_elevated_count += 1
            else:  # 130 and above
                bme_hypertensive_count += 1
        
        # Display category counts
        print("\n📊 CATEGORY DISTRIBUTION:")
        print("-" * 40)
        print(f"  Normal (<120 mmHg):        {bme_normal_count} day(s)")
        print(f"  Elevated (120-129 mmHg):   {bme_elevated_count} day(s)")
        print(f"  Hypertensive (≥130 mmHg):  {bme_hypertensive_count} day(s)")
        
        # Calculate percentages
        bme_total = len(self.bme_systolic_readings)
        if bme_total > 0:
            print(f"\n  📈 Percentage breakdown:")
            print(f"     Normal:      {(bme_normal_count/bme_total)*100:.1f}%")
            print(f"     Elevated:    {(bme_elevated_count/bme_total)*100:.1f}%")
            print(f"     Hypertensive: {(bme_hypertensive_count/bme_total)*100:.1f}%")
        
        # (b) Identify day with highest reading
        bme_highest_value = max(self.bme_systolic_readings)
        bme_highest_day = self.bme_systolic_readings.index(bme_highest_value) + 1  # +1 for 1-indexed
        
        print("\n🏆 HIGHEST READING:")
        print("-" * 40)
        print(f"  Day {bme_highest_day}: {bme_highest_value} mmHg")
        
        # Check for multiple days with same highest value
        bme_occurrences = [i + 1 for i, val in enumerate(self.bme_systolic_readings) if val == bme_highest_value]
        if len(bme_occurrences) > 1:
            print(f"  (Note: Also occurred on day(s): {', '.join(map(str, bme_occurrences[1:]))})")
        
        # (c) Check for consistently increasing trend
        bme_is_increasing = True
        bme_increasing_pairs = []
        bme_decreasing_pairs = []
        
        for bme_i in range(len(self.bme_systolic_readings) - 1):
            bme_current = self.bme_systolic_readings[bme_i]
            bme_next = self.bme_systolic_readings[bme_i + 1]
            
            if bme_next <= bme_current:
                bme_is_increasing = False
                bme_decreasing_pairs.append((bme_i + 1, bme_current, bme_next))
            else:
                bme_increasing_pairs.append((bme_i + 1, bme_current, bme_next))
        
        print("\n📉 TREND ANALYSIS:")
        print("-" * 40)
        
        if bme_is_increasing and len(self.bme_systolic_readings) > 1:
            print("  ⚠️  WORSENING TREND DETECTED!")
            print("     Blood pressure increased consistently across all days.")
            print("     Clinical follow-up recommended.")
        else:
            print("  ✅ No consistent worsening detected.")
            if bme_decreasing_pairs:
                print(f"\n     Non-increasing pairs found:")
                for bme_day, bme_curr, bme_next in bme_decreasing_pairs[:3]:  # Show first 3
                    print(f"       - Day {bme_day} → Day {bme_day + 1}: {bme_curr} → {bme_next} mmHg "
                          f"({bme_next - bme_curr:+.0f} change)")
                if len(bme_decreasing_pairs) > 3:
                    print(f"       ... and {len(bme_decreasing_pairs) - 3} more")
        
        # Additional statistics
        self._displayAdditionalStats()
        
        # Clinical recommendations
        self._displayRecommendations(bme_normal_count, bme_elevated_count, 
                                     bme_hypertensive_count, bme_highest_value)
        
        print("\n" + "=" * 60)
        print("End of Analysis Report")
        print("=" * 60)
    
    def _displayAdditionalStats(self):
        """Display additional statistical information"""
        bme_readings = self.bme_systolic_readings
        if not bme_readings:
            return
        
        bme_avg = sum(bme_readings) / len(bme_readings)
        bme_min = min(bme_readings)
        bme_max = max(bme_readings)
        bme_range = bme_max - bme_min
        
        print("\n📐 ADDITIONAL STATISTICS:")
        print("-" * 40)
        print(f"  Average BP:    {bme_avg:.1f} mmHg")
        print(f"  Minimum BP:    {bme_min} mmHg")
        print(f"  Maximum BP:    {bme_max} mmHg")
        print(f"  Range:         {bme_range} mmHg")
        
        # Calculate variability (standard deviation simplified)
        bme_variance = sum((x - bme_avg) ** 2 for x in bme_readings) / len(bme_readings)
        bme_std_dev = bme_variance ** 0.5
        print(f"  Std Deviation: {bme_std_dev:.1f} mmHg")
        
        if bme_std_dev > 15:
            print("  ⚠️  High variability detected - BP is unstable")
    
    def _displayRecommendations(self, bme_normal, bme_elevated, bme_hypertensive, bme_highest):
        """Generate clinical recommendations based on analysis"""
        print("\n💡 CLINICAL RECOMMENDATIONS:")
        print("-" * 40)
        
        bme_total = len(self.bme_systolic_readings)
        
        if bme_hypertensive > bme_total * 0.5:
            print("  🔴 URGENT: Majority of readings are in Hypertensive range.")
            print("     Immediate medical consultation required.")
        elif bme_hypertensive > 0:
            print("  🟠 CAUTION: Hypertensive readings detected.")
            print("     Schedule follow-up with cardiologist.")
        
        if bme_elevated > bme_total * 0.3:
            print("  🟡 Monitor: Elevated readings present in >30% of days.")
            print("     Lifestyle modifications recommended.")
        
        if bme_highest >= 180:
            print("  🔴 CRITICAL: Very high BP detected (≥180 mmHg).")
            print("     Emergency evaluation may be necessary.")
        elif bme_highest >= 160:
            print("  🟠 Severe elevation detected. Prompt medical review advised.")
        
        if bme_normal == bme_total:
            print("  ✅ Excellent! All readings are in normal range.")
            print("     Maintain healthy lifestyle.")
        elif bme_normal > 0:
            print("  ℹ️  Some normal readings observed. Continue monitoring.")
        
        print("  📋 General advice:")
        print("     - Reduce sodium intake")
        print("     - Regular exercise (as permitted by physician)")
        print("     - Stress management techniques")
        print("     - Regular BP monitoring")


# Main program - Test the Blood Pressure Tracker
print("🏥 BLOOD PRESSURE TREND ANALYSER")
print("Cardiology Department - Patient Monitoring System")
print("=" * 60)

# Create patient tracker
bme_patient = BPTracker("John Doe")

# Choose input method
print("\nChoose input method:")
print("1. Enter readings manually")
print("2. Use demo data")
bme_choice = input("Enter choice (1 or 2): ")

if bme_choice == "1":
    bme_days = int(input("How many days of readings? "))
    bme_patient.loadReadings(bme_days)
else:
    # Demo data covering all scenarios
    print("\n📊 Loading demo data...")
    
    # Test Case 1: Worsening trend
    print("\n" + "🎯" * 20)
    print("TEST CASE 1: Patient with worsening BP trend")
    print("🎯" * 20)
    bme_patient1 = BPTracker("Sir Zumair")
    bme_patient1.bme_systolic_readings = [118, 122, 125, 128, 131, 135]
    bme_patient1.bme_num_days = 6
    bme_patient1._displayReadings()
    bme_patient1.analyse()
    
    print("\n" + "🎯" * 20)
    print("TEST CASE 2: Patient with fluctuating BP")
    print("🎯" * 20)
    bme_patient2 = BPTracker("Sir Talha")
    bme_patient2.bme_systolic_readings = [115, 118, 125, 122, 130, 128, 135, 132]
    bme_patient2.bme_num_days = 8
    bme_patient2._displayReadings()
    bme_patient2.analyse()
    
    print("\n" + "🎯" * 20)
    print("TEST CASE 3: Patient with normal stable BP")
    print("🎯" * 20)
    bme_patient3 = BPTracker("Dr Zeeshan")
    bme_patient3.bme_systolic_readings = [110, 112, 115, 114, 116, 115]
    bme_patient3.bme_num_days = 6
    bme_patient3._displayReadings()
    bme_patient3.analyse()
    
    print("\n" + "🎯" * 20)
    print("TEST CASE 4: Patient with severe hypertension")
    print("🎯" * 20)
    bme_patient4 = BPTracker("Dr Jawad")
    bme_patient4.bme_systolic_readings = [145, 150, 155, 160, 158, 165, 170]
    bme_patient4.bme_num_days = 7
    bme_patient4._displayReadings()
    bme_patient4.analyse()

# If user chose manual entry for the main patient
if bme_choice == "1":
    bme_patient.analyse()