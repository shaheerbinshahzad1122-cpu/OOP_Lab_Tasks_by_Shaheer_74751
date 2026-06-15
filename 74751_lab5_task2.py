class MedicalSensor:
    def __init__(self, sensor_id="None", sensor_type="Unknown", calibration_factor=1.0, obj=None):
        if obj is not None and isinstance(obj, MedicalSensor):
            self.sensor_id = obj.sensor_id + "_copy"
            self.type = obj.type
            self.calibration_factor = obj.calibration_factor
            self.recent_readings = list(obj.recent_readings) # copy
        else:
            self.sensor_id = sensor_id
            self.type = sensor_type
            self.calibration_factor = calibration_factor
            self.recent_readings = []

    def __del__(self):
        print(f"Sensor {self.sensor_id} removed from the monitoring system.")

    def record_reading(self, value):
        self.recent_readings.append(value)

    def calculate_average(self):
        if not self.recent_readings:
            return 0.0
        return sum(self.recent_readings) / len(self.recent_readings)

    def calculate_peak(self):
        if not self.recent_readings:
            return 0.0
        return max(self.recent_readings)

    def apply_calibration_adjustment(self):
        self.recent_readings = [val * self.calibration_factor for val in self.recent_readings]
        print("Calibration applied to all recent readings.")

    def generate_sensor_report(self):
        print("--- Sensor Report ---")
        print(f"ID: {self.sensor_id} | Type: {self.type}")
        print(f"Calibration Factor: {self.calibration_factor}")
        print(f"Number of Readings: {len(self.recent_readings)}")
        print(f"Average Reading: {self.calculate_average():.2f}")
        print(f"Peak Reading: {self.calculate_peak():.2f}")

if __name__ == "__main__":
    s1 = MedicalSensor("S-01", "ECG", 1.05)
    s1.record_reading(12.5)
    s1.record_reading(14.2)
    s1.record_reading(13.8)
    
    s2 = MedicalSensor(obj=s1)
    
    s1.apply_calibration_adjustment()
    s1.generate_sensor_report()
