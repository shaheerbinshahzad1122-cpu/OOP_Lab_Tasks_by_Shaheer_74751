class BatteryBackup:
    def __init__(self, battery_id="Unknown", capacity=0.0, voltage=0.0, obj=None):
        if obj is not None and isinstance(obj, BatteryBackup):
            # Copy constructor behavior
            self.battery_id = obj.battery_id + "_copy"
            self.capacity = obj.capacity
            self.current_charge_level = obj.current_charge_level
            self.voltage = obj.voltage
        else:
            # Default and parameterized constructor
            self.battery_id = battery_id
            self.capacity = capacity
            self.current_charge_level = capacity
            self.voltage = voltage

    def __del__(self):
        print(f"System shutdown log: BatteryBackup object {self.battery_id} is being destroyed.")

    def charge_battery(self, amount):
        if amount > 0:
            self.current_charge_level += amount
            if self.current_charge_level > self.capacity:
                self.current_charge_level = self.capacity
            print(f"Battery charged. Current level: {self.current_charge_level} Ah")

    def discharge(self, amount):
        if amount > 0:
            if self.current_charge_level >= amount:
                self.current_charge_level -= amount
                print(f"Discharged {amount} Ah. Remaining: {self.current_charge_level} Ah")
            else:
                print("Safety Check Failed: Insufficient charge for this discharge amount.")

    def calculate_remaining_backup_time(self, current_load):
        if current_load > 0:
            return self.current_charge_level / current_load
        return 0.0

    def display_status(self):
        print("--- Battery Status ---")
        print(f"ID: {self.battery_id}")
        print(f"Capacity: {self.capacity} Ah")
        print(f"Current Charge Level: {self.current_charge_level} Ah")
        print(f"Voltage: {self.voltage} V")

if __name__ == "__main__":
    default_battery = BatteryBackup()
    b1 = BatteryBackup("UPS-101", 100.0, 12.0)
    b2 = BatteryBackup(obj=b1)

    b1.display_status()
    b1.discharge(20.0)
    b1.discharge(100.0)
    b1.charge_battery(10.0)
    print(f"Remaining backup time at 5A load: {b1.calculate_remaining_backup_time(5.0):.2f} hours")
