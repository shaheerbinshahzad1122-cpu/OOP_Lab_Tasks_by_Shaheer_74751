# ECG Signal Classifier
class ECGReading:
    def __init__(self, bme_rr_interval, bme_qrs_duration):
        """
        Constructor for ECG Reading
        Boundary decisions:
        - RR interval: >= 1000ms -> Bradycardic, < 1000ms -> Normal/Tachy
        - RR interval: <= 600ms -> Tachycardic, > 600ms -> Normal/Brady
        - QRS duration: > 120ms -> Wide, <= 120ms -> Narrow
        """
        self.bme_rr_interval = bme_rr_interval
        self.bme_qrs_duration = bme_qrs_duration
    
    def classify(self):
        """Classifies heart rhythm based on RR interval and QRS duration"""
        
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
        
        # Construct and print the full classification
        bme_classification = f"{bme_rhythm_type} {bme_qrs_label}"
        print(f"ECG Classification: {bme_classification}")
        print(f"  (RR: {self.bme_rr_interval}ms, QRS: {self.bme_qrs_duration}ms)")
        
        return bme_classification


# Test the ECG classifier with different combinations
print("=" * 60)
print("🏥 ECG SIGNAL CLASSIFIER - Rhythm Analysis System")
print("=" * 60)

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

print("\n" + "=" * 60)
print("Classification complete - All nested branches covered")
print("=" * 60)