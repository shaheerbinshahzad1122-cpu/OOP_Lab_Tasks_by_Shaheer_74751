import copy

class PatientMonitor:
    def __init__(self, monitor_id="UNKNOWN", patient_id="UNKNOWN", obj=None):
        if obj is not None and isinstance(obj, PatientMonitor):
            self.monitor_id = obj.monitor_id + "_copy"
            self.patient_id = obj.patient_id
            self.vital_signals = copy.deepcopy(obj.vital_signals)
        else:
            self.monitor_id = monitor_id
            self.patient_id = patient_id
            self.vital_signals = {}

    def __del__(self):
        print(f"Patient Monitor {self.monitor_id} detached from patient {self.patient_id}.")

    def add_signal_sample(self, channel, value):
        if channel not in self.vital_signals:
            self.vital_signals[channel] = []
        self.vital_signals[channel].append(value)

    def compute_average(self, channel):
        if channel in self.vital_signals and self.vital_signals[channel]:
            return sum(self.vital_signals[channel]) / len(self.vital_signals[channel])
        return 0.0

    def detect_abnormal_readings(self, channel, min_safe, max_safe):
        if channel in self.vital_signals:
            for val in self.vital_signals[channel]:
                if val < min_safe or val > max_safe:
                    print(f"ALERT: Abnormal reading {val} detected on channel {channel}!")

    def produce_monitoring_summary_report(self):
        print("--- Monitoring Summary Report ---")
        print(f"Monitor ID: {self.monitor_id} | Patient ID: {self.patient_id}")
        for channel, samples in self.vital_signals.items():
            print(f"Channel: {channel}")
            print(f"  - Samples: {len(samples)}")
            avg = sum(samples) / len(samples) if samples else 0.0
            print(f"  - Average: {avg:.2f}")
        print("---------------------------------")

if __name__ == "__main__":
    p1 = PatientMonitor("PM-01", "PT-1234")
    p1.add_signal_sample("HeartRate", 75.0)
    p1.add_signal_sample("HeartRate", 78.0)
    p1.add_signal_sample("HeartRate", 120.0) # Abnormal
    
    p1.add_signal_sample("Voltage", 12.1)
    p1.add_signal_sample("Voltage", 11.9)
    
    p2 = PatientMonitor(obj=p1) # Deep copy
    
    p1.detect_abnormal_readings("HeartRate", 60.0, 100.0)
    p1.produce_monitoring_summary_report()
