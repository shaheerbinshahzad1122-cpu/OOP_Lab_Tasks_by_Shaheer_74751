class Device:
    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption

class HospitalCircuit:
    def __init__(self, circuit_id="Unknown", voltage_rating=220.0, obj=None):
        if obj is not None and isinstance(obj, HospitalCircuit):
            self.circuit_id = obj.circuit_id + "_copy"
            self.voltage_rating = obj.voltage_rating
            self.current_load = obj.current_load
            self.connected_devices = [Device(d.name, d.power_consumption) for d in obj.connected_devices]
        else:
            self.circuit_id = circuit_id
            self.voltage_rating = voltage_rating
            self.current_load = 0.0
            self.connected_devices = []

    def __del__(self):
        print(f"Circuit {self.circuit_id} is taken offline.")

    def add_device(self, device_name, power):
        self.connected_devices.append(Device(device_name, power))
        self.current_load += power / self.voltage_rating
        print(f"Device {device_name} added.")

    def remove_device(self, device_name):
        for d in self.connected_devices:
            if d.name == device_name:
                self.current_load -= d.power_consumption / self.voltage_rating
                self.connected_devices.remove(d)
                print(f"Device {device_name} removed.")
                return
        print("Device not found.")

    def calculate_total_power_consumption(self):
        return sum(d.power_consumption for d in self.connected_devices)

    def check_for_overload(self, max_current_load):
        return self.current_load > max_current_load

    def display_circuit_information(self):
        print("--- Circuit Information ---")
        print(f"ID: {self.circuit_id} | Voltage: {self.voltage_rating} V")
        print(f"Current Load: {self.current_load:.2f} A")
        print(f"Connected Devices: {len(self.connected_devices)}")
        for d in self.connected_devices:
            print(f"  - {d.name} ({d.power_consumption} W)")

if __name__ == "__main__":
    c1 = HospitalCircuit("ICU-Wiring-01", 220.0)
    c1.add_device("Ventilator", 500.0)
    c1.add_device("Monitor", 100.0)
    
    c2 = HospitalCircuit(obj=c1)
    
    c1.display_circuit_information()
    print(f"Total Power Consumption: {c1.calculate_total_power_consumption()} W")
    
    if c1.check_for_overload(10.0):
        print("WARNING: Overload condition detected!")
    else:
        print("Circuit load is within safe limits.")
        
    c1.remove_device("Monitor")
