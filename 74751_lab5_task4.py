class DefibrillatorModule:
    def __init__(self, serial_number="UNKNOWN", battery_charge=0.0, maintenance_date="N/A", energy=0.0, obj=None):
        if obj is not None and isinstance(obj, DefibrillatorModule):
            self.serial_number = obj.serial_number + "_copy"
            self.battery_charge_percentage = obj.battery_charge_percentage
            self.last_maintenance_date = obj.last_maintenance_date
            self.energy_settings = obj.energy_settings
        else:
            self.serial_number = serial_number
            self.battery_charge_percentage = battery_charge
            self.last_maintenance_date = maintenance_date
            self.energy_settings = energy

    def __del__(self):
        print(f"Device Deactivation Log: Defibrillator {self.serial_number} is going offline.")

    def update_battery_charge(self, amount):
        self.battery_charge_percentage += amount
        if self.battery_charge_percentage > 100.0:
            self.battery_charge_percentage = 100.0
        if self.battery_charge_percentage < 0.0:
            self.battery_charge_percentage = 0.0
        print(f"Battery charge updated to {self.battery_charge_percentage}%")

    def set_energy_level(self, level):
        self.energy_settings = level
        print(f"Energy level set to {self.energy_settings} Joules.")

    def perform_self_test(self):
        print(f"Performing self-test on Defibrillator {self.serial_number}...")
        if self.battery_charge_percentage > 20.0:
            print("Self-test passed. Device is ready.")
        else:
            print("Self-test failed. Battery too low!")

    def calculate_estimated_remaining_uses(self):
        if self.energy_settings <= 0:
            return 0
        
        consume_per_use = (self.energy_settings / 200.0) * 5.0
        if consume_per_use <= 0:
            consume_per_use = 1.0
            
        return int(self.battery_charge_percentage / consume_per_use)

if __name__ == "__main__":
    d1 = DefibrillatorModule("DEF-9901", 100.0, "2023-10-01", 150.0)
    d2 = DefibrillatorModule(obj=d1)
    
    d1.perform_self_test()
    d1.update_battery_charge(-30.0)
    d1.set_energy_level(200.0)
    
    print(f"Estimated remaining uses: {d1.calculate_estimated_remaining_uses()}")
