# Lab Task 4: Rehabilliation Progress Tracker
class RehabTracker:
    def __init__(self, bme_num_joints, bme_num_sessions):
        """
        Constructor for Rehabilitation Tracker
        Creates a 2D structure: rows = joints, columns = sessions
        """
        self.bme_num_joints = bme_num_joints
        self.bme_num_sessions = bme_num_sessions
        # Initialize empty 2D list: joints × sessions
        self.bme_readings = [[0 for _ in range(bme_num_sessions)] for _ in range(bme_num_joints)]
    
    def enterReadings(self):
        """
        Uses nested loops to accept ROM values from user
        Structure: Outer loop iterates joints, inner loop iterates sessions
        """
        print("\n" + "=" * 60)
        print("📝 ENTER RANGE-OF-MOTION (ROM) READINGS")
        print("=" * 60)
        
        for bme_joint in range(self.bme_num_joints):
            print(f"\n--- Joint {bme_joint + 1} ---")
            for bme_session in range(self.bme_num_sessions):
                while True:  # Input validation loop
                    try:
                        bme_reading = float(input(f"  Session {bme_session + 1} ROM (degrees): "))
                        if bme_reading < 0 or bme_reading > 180:
                            print("  ⚠️  ROM should be between 0° and 180°. Please re-enter.")
                            continue
                        self.bme_readings[bme_joint][bme_session] = bme_reading
                        break
                    except ValueError:
                        print("  ⚠️  Invalid input. Please enter a number.")
        
        print("\n✅ All readings recorded successfully!")
    
    def analyseProgress(self):
        """
        Analyses progress for each joint:
        - Computes improvement from session 1 to final session
        - Flags any session reading below 30° as 'Low Mobility'
        """
        print("\n" + "=" * 60)
        print("📊 REHABILITATION PROGRESS ANALYSIS")
        print("=" * 60)
        
        # Outer loop: iterate through each joint
        for bme_joint in range(self.bme_num_joints):
            print(f"\n{'='*50}")
            print(f"🔍 JOINT {bme_joint + 1} ANALYSIS")
            print(f"{'='*50}")
            
            # Store first and last session values
            bme_first_reading = self.bme_readings[bme_joint][0]
            bme_last_reading = self.bme_readings[bme_joint][self.bme_num_sessions - 1]
            
            # Calculate improvement
            bme_improvement = bme_last_reading - bme_first_reading
            
            # Display progress summary
            print(f"  Initial ROM (Session 1):  {bme_first_reading}°")
            print(f"  Final ROM (Session {self.bme_num_sessions}):   {bme_last_reading}°")
            print(f"  Improvement:              {bme_improvement:+.1f}°")
            
            if bme_improvement > 0:
                print(f"  ✅ Progress: Improving")
            elif bme_improvement < 0:
                print(f"  ⚠️  Progress: Declining - Needs attention!")
            else:
                print(f"  → Progress: No change")
            
            # Inner loop: check each session for low mobility
            bme_low_mobility_count = 0
            print(f"\n  Session-by-session analysis:")
            
            for bme_session in range(self.bme_num_sessions):
                bme_reading = self.bme_readings[bme_joint][bme_session]
                
                # Flag low mobility readings (below 30°)
                if bme_reading < 30:
                    print(f"    ⚠️  Session {bme_session + 1}: {bme_reading}° - LOW MOBILITY WARNING!")
                    bme_low_mobility_count += 1
                else:
                    # Show normal readings with visual indicator
                    bme_status = "✓" if bme_reading >= 60 else "◔"
                    print(f"    {bme_status} Session {bme_session + 1}: {bme_reading}°")
            
            # Summary for this joint
            if bme_low_mobility_count > 0:
                print(f"\n  ⚠️  Total low mobility alerts: {bme_low_mobility_count}")
                print(f"  💡 Recommendation: Focused therapy needed for this joint")
            else:
                print(f"\n  ✅ No low mobility issues detected")
            
            # Progress trend indicator
            if bme_improvement >= 15:
                print(f"  🎉 Excellent improvement! (+{bme_improvement:.1f}°)")
            elif bme_improvement <= -10:
                print(f"  🚨 Significant decline detected! Immediate review recommended")
        
        print("\n" + "=" * 60)
        print("✅ Analysis complete")
        print("=" * 60)
    
    def displayAllReadings(self):
        """
        Optional helper method to display all readings in table format
        """
        print("\n" + "=" * 60)
        print("📋 COMPLETE ROM READINGS TABLE")
        print("=" * 60)
        
        # Print header
        print(f"{'Joint':<10}", end="")
        for bme_s in range(self.bme_num_sessions):
            print(f"S{bme_s+1:<8}", end="")
        print()
        print("-" * (10 + 8 * self.bme_num_sessions))
        
        # Print readings
        for bme_joint in range(self.bme_num_joints):
            print(f"Joint {bme_joint+1:<4}", end="")
            for bme_session in range(self.bme_num_sessions):
                print(f"{self.bme_readings[bme_joint][bme_session]:<8.1f}", end="")
            print()
        print("=" * 60)


# Main program - Test the Rehabilitation Tracker
print("🏥 REHABILITATION PROGRESS TRACKER")
print("Physiotherapy Clinic - ROM Monitoring System")

# Create tracker for 3 joints over 4 sessions
bme_tracker = RehabTracker(3, 4)

# Enter readings with sample data (or user input)
print("\n" + "=" * 60)
print("Would you like to:")
print("1. Enter readings manually")
print("2. Use demo data for testing")
bme_choice = input("Enter choice (1 or 2): ")

if bme_choice == "1":
    # Manual entry
    bme_tracker.enterReadings()
else:
    # Demo data for testing all conditions
    print("\n📊 Using demo data for testing...")
    
    # Demo readings: 3 joints × 4 sessions
    # Joint 1: Improving - starts low but shows good progress
    bme_tracker.bme_readings = [
        [25, 40, 55, 70],   # Joint 1: Low mobility initially, improving well
        [45, 42, 38, 35],   # Joint 2: Declining - needs attention
        [85, 88, 92, 95]    # Joint 3: Excellent, no issues
    ]
    
    print("Demo data loaded:")
    bme_tracker.displayAllReadings()

# Run the analysis
bme_tracker.analyseProgress()

# Additional test with different configurations
print("\n" + "🎯" * 20)
print("Additional Test: Different joint/session configuration")
print("🎯" * 20)

# Create a second tracker for 2 joints over 3 sessions
bme_tracker2 = RehabTracker(2, 3)
bme_tracker2.bme_readings = [
    [15, 28, 32],   # Joint 1: Improving but with low mobility
    [90, 85, 88]    # Joint 2: Stable with good ROM
]
bme_tracker2.displayAllReadings()
bme_tracker2.analyseProgress()