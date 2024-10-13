# EKSEMPELKODE FRA CHATGPT
# Skrur av og på systemet
# For å hente informasjon om selve enheten, så eksponeres mye av dette til holding registers

from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException

# Create Modbus RTU client
client = ModbusClient(
    method='rtu',
    port='/dev/ttyUSB0',  # Adjust this to your serial port
    baudrate=9600,
    stopbits=1,
    bytesize=8,
    parity='N',
    timeout=1
)

# Connect to the client
client.connect()

def turn_device_on(slave_id, coil_address):
    """Turn the Modbus device on by setting the coil to True (1)."""
    try:
        result = client.write_coil(coil_address, True, unit=slave_id)
        if result.isError():
            print("Failed to turn on the device.")
        else:
            print("Device turned on.")
    except ModbusException as e:
        print(f"Error: {e}")

def turn_device_off(slave_id, coil_address):
    """Turn the Modbus device off by setting the coil to False (0)."""
    try:
        result = client.write_coil(coil_address, False, unit=slave_id)
        if result.isError():
            print("Failed to turn off the device.")
        else:
            print("Device turned off.")
    except ModbusException as e:
        print(f"Error: {e}")

def get_information(slave_id, register_address):
    """Returns information exposed by the unit"""
    try:
        result = client.read_holding_registers(address=register_address, count=None, unit=slave_id)
        if result.isError():
            print("Failed to get information about device.")
        else:
            print("Information:")
            #TODO formatter hvordan informasjonen presenteres
    except ModbusException as e:
        print(f"Error: {e}")

def get_system_status(slave_id, register_address):
    "Returns information about healt, sensor values etc"
    try:
        result = client.read_input_registers(address=register_address, count=None, unit=slave_id)
        if result.isError():
            print("Failed to get device status.")
        else:
            print("Information:")
            #TODO formatter hvordan informasjonen presenteres
    except ModbusException as e:
        print(f"Error: {e}")


# Example usage
slave_id = 1           # The Modbus slave ID of your device
coil_address = 0       # The coil address controlling power (adjust as needed)

# Turn the device on
turn_device_on(slave_id, coil_address)

# Turn the device off
turn_device_off(slave_id, coil_address)

# Close the client connection
client.close()
